import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:universal_share/config/init.dart';
import 'package:universal_share/config/init_error.dart';
import 'package:universal_share/config/theme.dart';
import 'package:universal_share/gen/strings.g.dart';
import 'package:universal_share/model/persistence/color_mode.dart';
import 'package:universal_share/pages/home_page.dart';
import 'package:universal_share/provider/local_ip_provider.dart';
import 'package:universal_share/provider/network/server/server_provider.dart';
import 'package:universal_share/provider/settings_provider.dart';
import 'package:universal_share/util/native/platform_check.dart';
import 'package:universal_share/util/ui/dynamic_colors.dart';
import 'package:universal_share/widget/watcher/life_cycle_watcher.dart';
import 'package:universal_share/widget/watcher/shortcut_watcher.dart';
import 'package:universal_share/widget/watcher/tray_watcher.dart';
import 'package:universal_share/widget/watcher/window_brightness_watcher.dart';
import 'package:universal_share/widget/watcher/window_watcher.dart';
import 'package:localsend_isolates/isolate.dart';
import 'package:refena_flutter/addons.dart';
import 'package:refena_flutter/refena_flutter.dart';
import 'package:routerino/routerino.dart';
import 'package:system_date_time_format/system_date_time_format.dart';

Future<void> main(List<String> args) async {
  final RefenaContainer container;
  try {
    container = await preInit(args);
  } catch (e, stackTrace) {
    showInitErrorApp(
      error: e,
      stackTrace: stackTrace,
    );
    return;
  }

  runApp(
    RefenaScope.withContainer(
      container: container,
      child: SDTFScope(
        child: TranslationProvider(
          child: const Universal ShareApp(),
        ),
      ),
    ),
  );
}

class Universal ShareApp extends StatelessWidget {
  const Universal ShareApp();

  @override
  Widget build(BuildContext context) {
    final ref = context.ref;
    final (themeMode, colorMode, customColor) = ref.watch(
      settingsProvider.select((settings) => (settings.theme, settings.colorMode, settings.customColor)),
    );
    final dynamicColors = ref.watch(dynamicColorsProvider);
    return TrayWatcher(
      child: WindowWatcher(
        child: LifeCycleWatcher(
          onChangedState: (AppLifecycleState state) {
            switch (state) {
              case AppLifecycleState.resumed:
                ref.redux(localIpProvider).dispatch(InitLocalIpAction());
                if (checkPlatform([TargetPlatform.iOS, TargetPlatform.android])) {
                  // The OS may have invalidated the sockets of the suspended app without any error ever reaching the accept loop.
                  // ignore: discarded_futures
                  ref.notifier(serverProvider).ensureRunning();
                }
                if (checkPlatform([TargetPlatform.iOS])) {
                  // The multicast sockets die the same silent way but cannot be probed, so always rebind them.
                  ref.redux(parentIsolateProvider).dispatch(IsolateDiscoveryRestartAction());
                }
                break;
              case AppLifecycleState.detached:
                // The main isolate is only exited when all child isolates are exited.
                // https://github.com/yashhasan570/UniversalShare/issues/1568
                ref.redux(parentIsolateProvider).dispatch(IsolateDisposeAction());
                break;
              default:
                break;
            }
          },
          child: ShortcutWatcher(
            child: MaterialApp(
              title: t.appName,
              locale: TranslationProvider.of(context).flutterLocale,
              supportedLocales: AppLocaleUtils.supportedLocales,
              localizationsDelegates: GlobalMaterialLocalizations.delegates,
              debugShowCheckedModeBanner: false,
              theme: getTheme(colorMode, customColor, Brightness.light, dynamicColors),
              darkTheme: getTheme(colorMode, customColor, Brightness.dark, dynamicColors),
              themeMode: colorMode == ColorMode.oled ? ThemeMode.dark : themeMode,
              builder: (context, child) => WindowBrightnessWatcher(child: child!),
              navigatorKey: context.read(navigationProvider).key,
              home: RouterinoHome(
                builder: () => const HomePage(
                  initialTab: HomeTab.receive,
                  appStart: true,
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
