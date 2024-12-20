# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['duplicate_ui.py'],
    pathex=[],
    binaries=[],
    datas=[('logo.PNG', '.')],  # Correct case for the PNG file
    hiddenimports=['duplicate'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Game File Duplicator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity='certificate.pfx',
    entitlements_file=None,
    icon='logo.PNG',  # Correct case for the PNG file
    version='file_version_info.txt'
)
