# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Ellumination\\System\\ImageScripter\\EXE\\Start_Hub.py'],
             pathex=['C:\\Ellumination\\System\\ImageScripter\\Scripts'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Start_Hub',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Ellumination\\System\\ImageScripter\\EXE\\loading_eye.ico')
