import 'package:flutter/material.dart';
import 'package:universal_share/gen/strings.g.dart';
import 'package:universal_share/pages/debug/debug_page.dart';
import 'package:universal_share/widget/local_send_logo.dart';
import 'package:universal_share/widget/responsive_list_view.dart';
import 'package:routerino/routerino.dart';
import 'package:url_launcher/url_launcher.dart';

class AboutPage extends StatelessWidget {
  const AboutPage();

  static const _repoUrl = 'https://github.com/yashhasan570/UniversalShare';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(t.aboutPage.title),
      ),
      body: ResponsiveListView(
        padding: const EdgeInsets.symmetric(horizontal: 15),
        children: [
          const SizedBox(height: 20),
          const UniversalShareLogo(withText: true),
          Text(
            '© ${DateTime.now().year} Universal Share',
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 10),
          Text(t.aboutPage.description.join('\n\n')),
          const SizedBox(height: 20),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              TextButton(
                onPressed: () async {
                  await launchUrl(Uri.parse(_repoUrl), mode: LaunchMode.externalApplication);
                },
                child: const Text('Homepage'),
              ),
              TextButton(
                onPressed: () async {
                  await launchUrl(Uri.parse(_repoUrl), mode: LaunchMode.externalApplication);
                },
                child: const Text('Source Code (Github)'),
              ),
              TextButton(
                onPressed: () async {
                  await launchUrl(Uri.parse('https://t.me/johnconstantine570'), mode: LaunchMode.externalApplication);
                },
                child: const Text('Contact on Telegram'),
              ),
              TextButton(
                onPressed: () async {
                  await launchUrl(Uri.parse('https://www.apache.org/licenses/LICENSE-2.0'), mode: LaunchMode.externalApplication);
                },
                child: const Text('Apache License 2.0'),
              ),
              TextButton(
                onPressed: () async {
                  await context.push(() => const LicensePage());
                },
                child: const Text('License Notices'),
              ),
              TextButton(
                onPressed: () async {
                  await context.push(() => const DebugPage());
                },
                child: const Text('Debugging'),
              ),
            ],
          ),
          const SizedBox(height: 50),
        ],
      ),
    );
  }
}
