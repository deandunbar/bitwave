# -*- mode: python -*-
a = Analysis(['bitwave_start_server.py'],
             pathex=['/home/thorax/Documents/dev/hackathon/bitcoin2015/poc/bitwave/bitwave'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='bitwave_start_server',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='bitwave_start_server')
