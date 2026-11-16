#!/usr/bin/env python3
"""Re-apply the Universal Share rebrand after each upstream sync."""
import os, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DELETE = [
    'CLAUDE.md','AGENTS.md','CONTRIBUTING.md','CODE_SIGNING.md','CHANGELOG.md',
    '.github/FUNDING.yml','.github/ISSUE_TEMPLATE','.github/release-drafter.yml',
    '.github/dependabot.yml','.github/winget.yml',
    'app/lib/pages/donation','app/lib/provider/purchase_provider.dart',
    'app/lib/model/state/purchase_state.dart','app/lib/model/state/purchase_state.mapper.dart',
    'app/lib/pages/about/contributors.dart','app/lib/pages/about/packagers.dart',
    'app/lib/pages/about/translators.dart',
    'app/android/app/src/main/res/drawable/ic_launcher_foreground.xml',
]

REPL = [
    ('LocalSendLogo','UniversalShareLogo'),
    ('package:localsend_app/','package:universal_share/'),
    ('org.localsend.localsendApp','com.universalshare.app'),
    ('org.localsend.localsend_app','com.universalshare.app'),
    ('localsend_app','universal_share'),
    ('https://localsend.org/privacy','https://github.com/yashhasan570/UniversalShare'),
    ('https://localsend.org','https://github.com/yashhasan570/UniversalShare'),
    ('https://codeberg.org/localsend/localsend','https://github.com/yashhasan570/UniversalShare'),
    ('https://github.com/localsend/localsend','https://github.com/yashhasan570/UniversalShare'),
    ('github.com/localsend/localsend','github.com/yashhasan570/UniversalShare'),
    ('localsend.org','github.com/yashhasan570/UniversalShare'),
    ('github.com/Tienisto','github.com/yashhasan570'),
    ('Tien Do Nam (@Tienisto)','yashhasan570 (@johnconstantine570)'),
    ('Tien Do Nam','yashhasan570'),
    ('Tienisto','johnconstantine570'),
    ('LocalSend','Universal Share'),
]

EXTS = {'.dart','.json','.md','.yaml','.yml','.xml','.plist','.xcconfig','.rc',
        '.toml','.rs','.sh','.properties','.gradle','.kts','.txt','.html','.js',
        '.ts','.mod','.lock','.cmake'}
SKIP_DIRS = {'.git','build','.dart_tool','node_modules'}
PROTECT = ('sync.yml',)  # keep the upstream clone URL intact

def main():
    # sync.yml replaces upstream's workflows wholesale; re-delete the dropped ones
    wf = ROOT/'.github'/'workflows'
    for p in wf.glob('*.yml'):
        if p.name not in ('build_android_apk.yml','ci.yml','sync.yml'):
            p.unlink()
    for rel in DELETE:
        p = ROOT/rel
        if p.is_dir(): shutil.rmtree(p, ignore_errors=True)
        elif p.exists(): p.unlink()

    changed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn in PROTECT: continue
            p = Path(dirpath)/fn
            if p.suffix.lower() not in EXTS: continue
            try: s = p.read_text(encoding='utf-8')
            except Exception: continue
            o = s
            for a, b in REPL:
                s = s.replace(a, b)
            if s != o:
                p.write_text(s, encoding='utf-8')
                changed += 1
    print(f'migrate: {changed} files updated')

if __name__ == '__main__':
    main()
