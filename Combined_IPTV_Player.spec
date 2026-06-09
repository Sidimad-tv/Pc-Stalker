# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['combined_launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('STALKER PLAYER.py', '.'), ('stalker.py', '.'), ('Epg.py', '.'), ('XTREME-IPTV-PLAYER/XTREME IPTV PLAYER BY MY-1 v4.0.py', 'XTREME-IPTV-PLAYER')],
    hiddenimports=['dateutil', 'dateutil.parser', 'dateutil.tz', 'lxml', 'lxml.etree', 'qdarkstyle', 'pytz', 'tqdm'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Combined_IPTV_Player',
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
)
