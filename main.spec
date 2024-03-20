# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Background.png', '.'), ('fish.png', '.'), ('shark.png', '.'), ('orange_krill.png', '.'), ('purple_krill.png', '.'), ('favicon.icns', '.'), ('scores.txt', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['favicon.ico'],
)
app = BUNDLE(
    exe,
    name='main.app',
    icon='favicon.ico',
    bundle_identifier=None,
)
