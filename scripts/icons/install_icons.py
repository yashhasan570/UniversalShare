#!/usr/bin/env python3
"""Regenerate every icon slot of Universal Share from scripts/icons/badge.png."""
from PIL import Image, ImageDraw
from pathlib import Path
import os, glob

ROOT = Path(__file__).resolve().parent.parent  # repo root
badge_src = Image.open(Path(__file__).parent / 'badge.png').convert('RGB')
badge = badge_src.resize((1024, 1024), Image.LANCZOS)

def size_of(p):
    try:
        with Image.open(p) as im: return im.size
    except Exception:
        return None

def repl(path, mode='square'):
    p = ROOT / path
    if not p.exists(): return
    sz = size_of(p) or (256, 256)
    if mode == 'inset':
        canvas = Image.new('RGBA', sz, (0, 0, 0, 0))
        inner = int(min(sz) * 0.62)
        canvas.paste(badge.resize((inner, inner), Image.LANCZOS), ((sz[0]-inner)//2, (sz[1]-inner)//2))
        canvas.save(p)
    else:
        badge.resize(sz, Image.LANCZOS).save(p)

# Create missing Android icon slots (blank, correct sizes) so the manifest
# always has the resources it references, even after a fresh setup.
_DENS = {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}
_FG = {'mdpi': 108, 'hdpi': 162, 'xhdpi': 216, 'xxhdpi': 324, 'xxxhdpi': 432}
_QT = {'mdpi': 24, 'hdpi': 36, 'xhdpi': 48, 'xxhdpi': 72, 'xxxhdpi': 96}
for _d, _sz in _DENS.items():
    _base = ROOT / f'app/android/app/src/main/res/mipmap-{_d}'
    for _name, _s in [('ic_launcher.png', _sz), ('ic_launcher_round.png', _sz),
                      ('ic_launcher_foreground.png', _FG[_d]),
                      ('ic_launcher_monochrome.png', _FG[_d]),
                      ('ic_launcher_quicktile_foreground.png', _QT[_d])]:
        _p = _base / _name
        if not _p.exists():
            _base.mkdir(parents=True, exist_ok=True)
            Image.new('RGBA', (_s, _s), (0, 0, 0, 0)).save(_p)
_banner = ROOT / 'app/android/app/src/main/res/drawable/banner.png'
if not _banner.exists():
    _banner.parent.mkdir(parents=True, exist_ok=True)
    Image.new('RGBA', (320, 180), (0, 0, 0, 0)).save(_banner)
_adaptive = ROOT / 'app/android/app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml'
if not _adaptive.exists():
    _adaptive.parent.mkdir(parents=True, exist_ok=True)
    _adaptive.write_text(
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
        '    <background android:drawable="@color/ic_launcher_background"/>\n'
        '    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>\n'
        '    <monochrome android:drawable="@mipmap/ic_launcher_monochrome"/>\n'
        '</adaptive-icon>\n')

for n in ['logo-32.png','logo-32-black.png','logo-32-white.png','logo-128.png',
          'logo-256.png','logo-512.png','logo-512-white.png']:
    repl(f'app/assets/img/{n}')

ico_sizes = [(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)]
img0 = badge.resize((256,256), Image.LANCZOS)
for dest in ['app/assets/img/logo.ico','app/assets/packaging/logo.ico',
             'app/windows/runner/resources/app_icon.ico']:
    if os.path.exists(ROOT/dest):
        img0.save(ROOT/dest, format='ICO', sizes=ico_sizes)

for p in glob.glob(str(ROOT/'app/android/app/src/main/res/mipmap-*/ic_launcher*.png')):
    name = os.path.basename(p)
    if 'monochrome' in name: continue
    if 'foreground' in name or 'quicktile' in name:
        repl(os.path.relpath(p, ROOT), mode='inset')
    else:
        repl(os.path.relpath(p, ROOT))

def circle(im):
    im = im.convert('RGBA')
    mask = Image.new('L', im.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, im.size[0]-1, im.size[1]-1), fill=255)
    out = Image.new('RGBA', im.size, (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out

for p in glob.glob(str(ROOT/'app/android/app/src/main/res/mipmap-*/ic_launcher_round.png')):
    sz = size_of(p) or (192, 192)
    circle(badge.resize(sz, Image.LANCZOS)).save(p)

repl('app/android/app/src/main/res/drawable/banner.png')

for p in glob.glob(str(ROOT/'app/ios/Runner/Assets.xcassets/AppIcon.appiconset/*.png')):
    repl(os.path.relpath(p, ROOT))
for p in glob.glob(str(ROOT/'app/macos/Runner/Assets.xcassets/**/*.png'), recursive=True):
    repl(os.path.relpath(p, ROOT))
try:
    badge.save(ROOT/'app/macos/ShareExtension/icon.icns', format='ICNS')
except Exception as e:
    print('icns failed:', e)

for p in ['app/web/favicon.png','app/web/icons/Icon-192.png','app/web/icons/Icon-512.png']:
    repl(p)
for p in ['app/web/icons/Icon-maskable-192.png','app/web/icons/Icon-maskable-512.png']:
    fp = ROOT / p
    if not fp.exists(): continue
    sz = size_of(fp) or (192, 192)
    canvas = Image.new('RGBA', sz, (10, 14, 26, 255))
    inner = int(min(sz) * 0.6)
    canvas.paste(badge.resize((inner, inner), Image.LANCZOS), ((sz[0]-inner)//2, (sz[1]-inner)//2))
    canvas.save(fp)

print('icons regenerated')
