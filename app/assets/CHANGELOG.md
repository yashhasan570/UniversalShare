## Unreleased

- fix(linux): tray icon fails to load in Snap installations (@vicajilau)
- fix: avoid adding a trailing dot when renaming files without an extension (@ShlomoCode)
- fix(macos): prevent intermittent MissingPluginException during startup (@ShlomoCode)
- fix(macos): file sharing via Share Extension doesn't work in DMG builds (@ShlomoCode, @vdmkotai)
- fix: show the real error when a file cannot be read while sending, instead of transferring it as an empty file (@leopalmieri-spec)
- fix: show the actual save location path for receiving files (@ShlomoCode)

## 1.18.2 (2026-08-21)

- feat: drag and drop files into the "Receive via link" browser page
- feat(desktop): allow customizing the web share pages by placing HTML files in a `web` folder next to the executable
- feat(cli): add version info to the Windows executable
- feat(linux): set actual version in the AppImage
- security: do not follow HTTP redirects sent by peers
- fix: restore compatibility with 1.17.0 and earlier versions on missing multicast networks
- fix: devices running 1.17.0 and earlier could not add 1.18.0+ device as favorite
- fix: ignore proxies, fixes "TLS info not found" when a system proxy (e.g. Shadowrocket) is enabled
- fix: automatically restart the HTTP / multicast server when it dies or when the app resumes
- fix: drag and drop with a mix of folders and files
- fix: during transfer, add bottom padding when Advanced is open (@Chethan616)
- fix: do not crash at startup when the executable path cannot be resolved (@Shlomo116)
- fix(android): ignore unknown or invalid file modification times when reading files
- i18n: add Armenian

## 1.18.1 (2026-08-11)

Android+iOS only hotfix update.

- fix: revert button icon sizes to 24
- fix: when sending a message that is accepted immediately, a ghost device list tile appears
- fix(mobile): when sending a link message, the "Open" button overflows
- fix(android): add missing ACCESS_LOCAL_NETWORK permission that is required for Android 17+
- i18n: add Belarusian (@pavel-miniutka), Irish (@aindriu80)

## 1.18.0 (2026-08-10)

- feat(cli): initial CLI release
- feat: receive via link
- feat: custom color theme via color picker
- feat: ipv6 support
- feat: checksum support (enabled by default)
- feat: automatically accept files by favorite devices by default
- feat: use decimal units for file sizes (1 GB = 1000 MB) to match macOS, iOS, Android, and Linux
- feat: enable starting text share via command line using `--text` or `-t` flags (@guilhermetiscoski)
- feat: improve remaining time formatting for long transfers (@ShlomoCode)
- feat: change duplicate file naming from "file-1.txt" to "file (1).txt" format (@kartoshka95)
- feat(android, ios, macos): respect system-wide animation preferences on first app startup (@nitheesh-daram)
- feat(android): run file transfer in background
- feat(android): add quick settings tile for instant app launch (@Voltra)
- feat(windows): add Universal Share to share sheet (@chenxdust)
- feat(macos): implement button to quickly open firewall settings from troubleshoot page (@ShlomoCode)
- feat(macos): add Command+Comma shortcut to open settings (@ShlomoCode)
- feat(macos): use user-friendly ComputerName instead of the technical hostname (@ShlomoCode)
- feat(macos): enable Dock icon text-drop even when the app is not running (@ShlomoCode)
- feat(linux): use native window decorations instead of large GTK3 headerbar (@nixigaj)
- perf: faster transfers for slow receiving devices
- fix: receiving / sending many files no longer freeze / lag
- fix: release wake lock after file transfer completes to allow device sleep (@kartoshka95)
- fix: text message content displayed three times in history dialog (@ew-sirenko)
- fix: text message content size calculation (@ew-sirenko)
- fix: save DNG files to image gallery (@ShlomoCode)
- fix(ios, android): prevent transfer error by saving unsupported media formats to folder instead of gallery (@ShlomoCode)
- fix(android): share to Universal Share sometimes doesn't work
- fix(android): preserve location metadata when sharing media (@ShlomoCode)
- fix(macos): prevent Dock icon from briefly appearing during autostart when "Start hidden" is enabled (@ShlomoCode)
- fix(macos): Dock icon drag-and-drop and Share Extension working again (@ShlomoCode)
- fix(linux): add CJK font support for Chinese, Japanese, and Korean text (@Mr-Ebonycat)

## 1.17.0 (2025-02-19)

- feat: add advanced setting to filter network interfaces (@johnconstantine570)
- feat(mobile): swipe gesture to select multiple media files (@johnconstantine570)
- feat(windows): when pasting an image, automatically convert it to PNG (@BrianMwit)
- feat(android): add option to open gallery when image/video was automatically saved (@johnconstantine570)
- fix: path traversal vulnerability when saving files (@johnconstantine570)
- fix: black screen when tapping on "Back" twice in "Share via link" (@johnconstantine570)
- fix(macos): window disappears on command key when minimize to tray is enabled (@johnconstantine570)
- fix(windows): do not poll local IP resulting in unwanted location permissions (@johnconstantine570)

## 1.16.2 (2024-11-06)

- fix(ios): share from other apps to Universal Share doesn't work in iOS 18 (@johnconstantine570)

## 1.16.1 (2024-11-05)

- feat: show exact error message when using IP address dialog or favorite dialog (@johnconstantine570)
- feat(desktop): highlight file when tapping "Show in folder" (@johnconstantine570)
- fix(android): properly close app on back gesture (@johnconstantine570)

## 1.16.0 (2024-11-03)

- feat: improve transfer speed if the sending device is the bottleneck by using Rust as HTTP client and multithreading (@johnconstantine570)
- feat: add option to automatically receive files only from favorites (@Davte)
- feat: only automatically finish when files are either successfully received or skipped (@johnconstantine570)
- feat: improve various padding and spacing issues in RTL languages (@ShlomoCode)
- feat: persist "advanced settings" toggle (@Nolle10)
- feat: add alias-regeneration button and alias update dialog (@Nolle10)
- feat(macos): drag-and-drop files and text into menu bar icon (@ShlomoCode)
- feat(macos): drag-and-drop text into the app icon (@ShlomoCode)
- feat(macos): include Universal Share as a share target in the share menu (@ShlomoCode)
- feat(macos): starts hidden in menu bar instead of being minimized when autostart is enabled (@ShlomoCode)
- feat(macos): show error and success state in the app icon (@ShlomoCode, @johnconstantine570)
- feat(macos): also have autostart option in sandboxed version (App Store) (@ShlomoCode)
- feat(macos): Universal Share installed via dmg installer is sandboxed (@johnconstantine570)
- feat(android): enable clipboard button (@Seidko)
- feat(ios): enable clipboard button (@AnessZurba)
- fix(macos): reopen app from launchpad after minimizing to menu bar should make window visible (@ShlomoCode)
- fix(macos): persist write access to download location after app restart (@ShlomoCode)
- i18n: add Malaysian (@Gloridust), Slovak (@dodog)

## 1.15.4 (2024-08-20)

- feat: add button to retry a failed file transfer (@johnconstantine570)
- feat: show tooltip on the "Scan" button (@johnconstantine570)
- feat: treat any URI as link, so it becomes clickable on receiver (e.g. file://, obsidian://) (@johnconstantine570)
- feat(mobile): adjust button width in send tab to indicate that it's scrollable (@johnconstantine570)
- feat(windows): title bar color should match the system theme (@FutoTan)
- fix: memory leak when sending files (regression in 1.15.0, 1.15.2 only fixed receiving files) (@johnconstantine570)
- fix(windows): Universal Share window is invisible at app start (@johnconstantine570)
- i18n: distinguish between "Exit" and "Quit" depending on the platform (@sergd88)
- i18n: add Hindi (@rishi-singh26)

## 1.15.3 (2024-07-29)

- feat: reduce receive history length to 30 items to increase performance (@johnconstantine570)
- feat: show error message when initialization fails for better debugging (@johnconstantine570)
- fix(android): properly close app on back gesture (@johnconstantine570)

## 1.15.2 (2024-07-25)

- feat: extract network scanning to separate threads, scanning should not cause UI lags anymore (@johnconstantine570)
- feat(windows): use bigger icon for the installer (@johnconstantine570)
- fix: memory leak when receiving files, properly receive files that exceed available RAM (@johnconstantine570)
- fix(android): save files outside of Download folder (@johnconstantine570)
- fix(windows): use correct portable settings file when started via autostart (@johnconstantine570)
- fix(windows): make installer work on arm64 (@johnconstantine570)

## 1.15.1 (2024-07-18)

- feat: support Internet Explorer 8 (IE8) in web share (@johnconstantine570)
- feat: save auto accept state when switching encryption mode in web share (@johnconstantine570)
- feat: switch to "Send" tab when pasting via keyboard shortcut (@johnconstantine570)
- fix: count PIN tries correctly in web share (@johnconstantine570)
- fix(android): crash when picking files or folders on Android TV (@johnconstantine570)
- fix(windows): crash when sum of file sizes is greater than 2 GB (@johnconstantine570)
- fix(windows): bundle required DLL files to avoid crash on app start (@johnconstantine570)
- fix(macos): hide autostart option when installed via App Store because this switch is not working (@johnconstantine570)

## 1.15.0 (2024-07-15)

- feat: add clear button in the send tab (@Caesarovich)
- feat: save text messages to history (@johnconstantine570)
- feat: keep timestamps of transferred files (@johnconstantine570)
- feat: add option to require PIN when sharing via link (@johnconstantine570)
- feat: add option to require PIN when receiving files (@johnconstantine570)
- feat: add option to open parent folder of received files in history (@johnconstantine570)
- feat: confirm before adding or removing favorites in the nearby devices list (@johnconstantine570)
- feat: add URL view when sharing via link that shows the URL in bigger font (@harriseldon)
- feat: add discovery timeout setting for advanced users (@o2e)
- feat(android): do not require MANAGE_EXTERNAL_STORAGE, implement Android SAF (@johnconstantine570)
- feat(android): do not copy files to cache when select via file picker (@johnconstantine570)
- feat(windows): add context menu integration ("Send to") (@johnconstantine570)
- feat(windows): toggle "start hidden" in-app instead of referring to the system settings (@johnconstantine570)
- feat(desktop): make auto start + start hidden more stable, now listens to `--hidden` parameter instead of `autostart` (@johnconstantine570)
- feat(desktop): load initial files from command line arguments (@johnconstantine570)
- feat(desktop): show progress in the taskbar (@NightFeather0615)
- feat(macos): handle files that were dropped into the app icon (@johnconstantine570)
- fix: sanitize file names with invalid characters (@Caesarovich)
- fix: UI overflow when window height is too small (@CHUNG-HAO)
- fix(ios): make documents files visible to the Finder / AppleDevices app (@twinkles-twinstar)
- fix(windows): correctly remove tray icon when closing the app (@zpp0196)
- fix(windows): don't keep file open (@NightFeather0615)
- fix(linux): compatibility with newer libayatana versions (@ix5)
- i18n: add Serbian (@nebojsatomic), Finnish (@jooapa), Romanian (@UnifeGi)

## 1.14.0 (2024-02-26)

- feat: add option to automatically accept requests when sharing via link (@MisterChangRay, @johnconstantine570)
- feat: use fix button width for all buttons in the selection row (only noticeable in Russian) (@johnconstantine570)
- fix: picking many files should not freeze the UI (@johnconstantine570)
- fix: do not create a new session for the same IP when sharing via link (@MisterChangRay)
- fix(android): save files to SD card on Android 10 or older (@johnconstantine570)
- i18n: add Danish (@Limfjorden)

## 1.13.1 (2023-12-08)

- feat: add a short delay when "Auto Finish" is enabled (@johnconstantine570)
- feat: automatically update the device name of favorite devices when they were unchanged by the user (@johnconstantine570)
- feat: expand file picker buttons if the button text is too long (@johnconstantine570)
- fix: various crash issues by downgrading Flutter from 3.16 to 3.13 (@johnconstantine570)

## 1.13.0 (2023-12-04)

- feat: add option to automatically finish after successful transfer (@johnconstantine570)
- feat: show favorite name in the device list if marked as favorite (@johnconstantine570)
- feat: ignore duplicate files when selected from file picker (@programmermager)
- feat: add donation options (@johnconstantine570)
- feat: add Yaru theme (@johnconstantine570)
- feat(desktop): uses `settings.json` located next to the executable if available for portable mode (@johnconstantine570)
- feat(windows): make windows icon sharper (@johnconstantine570, @sergd88)
- feat(macos): add Command+W shortcut to close the window (@Q1CHENL)
- fix: also show an OLED color mode option when dynamic colors are not supported by OS (@dhruvanbhalara)
- fix: sync button should spin right away when clicked (@johnconstantine570)
- fix(android): request permission when saving files outside of downloads folder (@johnconstantine570)
- fix(ios): fix permission error when picking directory (@johnconstantine570)
- fix(ios): clear cache when file is shared from another app (@johnconstantine570)
- i18n: add Greek (@multipetros), Khmer (@nidexingg)

## 1.12.0 (2023-10-25)

- feat: add favorites (@johnconstantine570)
- feat: add OLED color mode (@johnconstantine570)
- feat: show dialog before clearing history (@pantshaswat, @johnconstantine570)
- feat: show clear button in apk picker search bar (@johnconstantine570)
- feat: use better colors for the toggle switches in the settings (@gitstart)
- feat: drastically improve GPU usage by optimizing the spin animation (@johnconstantine570)
- feat(desktop): support pasting from clipboard (@gitstart, @johnconstantine570)
- feat(linux): allow disabling client side decorations on Wayland (@I-Want-ToBelieve)
- feat(android): use high framerate on devices that lock at 60 Hz like on some OnePlus phones (@johnconstantine570)
- fix(desktop): fallback to "$HOME/Downloads" when default downloads folder is unavailable (@Sqbika)
- i18n: add Vietnamese (@faea726), Thai (@watchakorn-18k), Basque (@xezpeleta)

## 1.11.1 (2023-09-04)

- feat: hide color setting when dynamic colors are not supported (@johnconstantine570)
- feat(linux): use white icon for the linux tray (@GaryElshaw, @johnconstantine570)
- fix: possible race condition leading to zero total files (@johnconstantine570)
- fix(android): navigation bar color on Android 9 and earlier (@johnconstantine570)
- fix(android): add `requestLegacyExternalStorage` again (that was removed in 1.11.0) (@johnconstantine570)
- fix(linux): do not use zenity dependency anymore for file picker (@johnconstantine570)

## 1.11.0 (2023-08-28)

- feat: optionally enable HTTPS (encryption) when share via link (@johnconstantine570)
- feat: use switches instead of dropdowns for settings (@forecaster-cyber)
- feat: tapping on scan button clears found devices (@johnconstantine570)
- feat: text message dialog is multiline only (@johnconstantine570)
- feat: add option to disable animations (@johnconstantine570)
- feat: add option to not save to history (@johnconstantine570)
- feat: add option to customize device model (@johnconstantine570)
- feat(desktop): bind "ESC" key to go to the previous page (@RiverTwilight, @johnconstantine570)
- feat(android, ios): open link in new browser tab (@johnconstantine570)
- feat(linux): enable autostart feature (@TheGB0077)
- fix(android, ios): Save GIFs and image metadata (@natsuk4ze)
- fix(android, ios): handle decline permission when picking files (@johnconstantine570)
- fix(desktop): GPU usage when hidden to tray (@johnconstantine570)

## 1.10.0 (2023-06-02)

- feat: dynamic colors (Material You) (@johnconstantine570)
- feat(android): sharing APKs includes version in file name (@johnconstantine570)
- feat(windows): restore Windows 7 support (@johnconstantine570)
- feat(windows): use specialized fonts for Chinese, Japanese and Korean (@graphemecluster, @johnconstantine570)
- fix: cancellation fixes during active file transfer (@SelaseKay)
- fix(windows): possible settings corruption (@TheGB0077, @johnconstantine570)
- fix(android): get downloads directory correctly (@johnconstantine570)
- fix(ios): could not save HEIC files (@johnconstantine570)

## 1.9.1 (2023-05-05)

- feat: add folder should include the folder itself
- fix: handle file names with special characters in link share mode
- fix(android): fix status bar icon color after picking a media file
- fix(linux): add libayatana-appindicator3-1 to AppImage dependencies (by @TheGB0077)

## 1.9.0 (2023-04-23)

- feat: directory share
- feat: share via browser link (for non-Universal Share users)
- feat: add "delete from history" button when file could not be opened (by @TheGB0077)
- feat: close message request when copied / opened link
- feat: slightly improve transfer speed
- feat: implement Universal Share protocol v2 with v1 fallback
- feat: scan (sync) button automatically scans all network interfaces when count < 3
- feat(android, ios): add "Save to gallery" setting button in file receive options
- feat(desktop): move troubleshoot out of navigation into send page
- feat(desktop): save last window position (by @TheGB0077)
- feat(android): enable edge-to-edge mode
- feat(android): add monochrome app icons for Android 13 (by @h9419)
- feat(android): set custom download path
- feat(linux): enable system tray (by @TheGB0077)
- fix: in multi-recipient mode, retrying causes a "canceled by sender" on the recipient device
- fix: clear selection after finished message transfer
- fix(ios): could not scan local network on iOS 14+ (by @TheGB0077)
- fix(android, ios): fallback asset picker strings to English translation (by @TheGB0077)
- fix(linux): header bar glitches
- i18n: add fa

## 1.8.0 (2023-03-05)

- feat: add send modes (single recipient, multiple recipients)
- feat: selection gets cleared after finish by default (part of send modes feature)
- feat: share to multiple recipients in parallel
- feat: add troubleshoot page
- feat: add 2 buttons to receive history: open folder + delete history
- feat: cleanup scan UI by hiding multiple network interfaces inside the scan button
- feat: edit text message in selected files
- feat: improve device discovery by answering with TCP instead of UDP
- feat(ex. iOS): pressing destination directory in progress page will open the directory
- feat(android): share apk and install apk
- feat(android): Android TV support
- feat(android): show loading indicator when picking (large) files
- feat(windows): left click on tray icon opens app
- feat(linux): add Control+Q shortcut to exit app
- fix: handshake error in unencrypted mode
- fix: also scan multicast when pressing on a subnet sync button
- fix(android): missing app icon on Android 7
- fix(android,ios): show error message when saving to gallery failed
- i18n: add bn, nl, uk

## 1.7.0 (2023-02-11)

- feat: improve device discovery by enabling multicast
- feat: received files history
- feat: show recent IP addresses in manual IP input
- feat: separate language settings page
- feat: message input is horizontally scrollable when multiline is unselected
- feat: open message normally in QuickSave mode (instead of saving it into a file)
- feat: improve error handling and add possibility to show exact error message for debugging
- feat: add unencrypted HTTP mode (for debugging)
- feat(android): keep file name when saving to photos
- feat(desktop): use bigger default window size if display is big enough
- feat(windows): use "Microsoft YaHei UI" font in Windows which works better with Chinese characters
- fix: cache cleanup on iOS
- i18n: add ar, es-ES, fr-FR, hu, in, it, iw, ja, ko, ne, pl, pt-BR, ru, sv, tr, zh-Hant-HK, zh-Hant-TW (Thanks to all the contributors!)

## 1.6.2 (2023-01-28)

- fix(desktop): close current instance when another is already open
- fix: cannot receive files when Chinese language is active
- fix(android, ios): share files with non-English names

## 1.6.1 (2023-01-27)

- fix(windows): app crashes when minimized to tray
- fix(android, ios): share intent sometimes not working
- fix(android, ios): scan not triggered when coming from share intent
- fix(android, ios): share intent produced duplicates after finishing a transfer

## 1.6.0 (2023-01-27)

- feat: show thumbnail in progress page
- feat: improve cache clearing mechanism
- feat: hashtag input now tries all combinations when multiple subnets are given
- feat(desktop): show dialog instead of bottom sheet when adding files
- feat(windows, mac): minimize to tray
- feat(windows): launch on login
- feat: add multiline toggle to message input
- fix: show correct file count in progress page
- fix: add self-discovering prevention
- i18n: add Simplified Chinese

## 1.5.2 (2023-01-14)

- F-Droid Release

## 1.5.1 (2023-01-10)

- fix(windows): app sometimes crash on start

## 1.5.0 (2023-01-09)

- feat: quick save mode
- feat: accept requests partially
- feat: set destination directory during accept phase
- feat: rename incoming files
- feat: keep screen on during file transfer
- feat: tap to open selected file before sending

## 1.4.0 (2023-01-06)

- feat: support multiple local IP addresses
- feat: detect if message is a link and add a button to open the link

## 1.3.1 (2023-01-03)

- fix: local IP sometimes not found

## 1.3.0 (2023-01-03)

- feat: enter custom target address
- feat: tap to open received file
- feat: responsive UI
- feat(ios): receive share intent
- feat(windows): set destination folder
- fix: update nearby device attributes when scan again

## 1.2.0 (2022-12-31)

- feat: drag and drop files
- feat: share plain messages
- feat(android): receive share intent

## 1.1.0 (2022-12-30)

- feat(android): add media picker
- feat(ios): merge image and video to common media picker
- fix(android): missing internet permission

## 1.0.0 (2022-12-29)

- Initial Release
