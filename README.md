# Universal Share

Share files across devices over your local network — no internet needed, no accounts, no ads.

Universal Share is a cross-platform app (Windows, macOS, Linux, Android, iOS, web) that lets you send files, messages, and media directly between nearby devices.

## Contact

Questions or feedback? Reach us on Telegram: [@johnconstantine570](https://t.me/johnconstantine570)

## Building

This is a Flutter project:

```
cd app
flutter pub get
flutter run
```

## Sync

`.github/workflows/sync.yml` pulls upstream changes daily, re-applies the Universal Share branding via `scripts/migrate.py`, and refreshes the icon set via `scripts/icons/install_icons.py`.
