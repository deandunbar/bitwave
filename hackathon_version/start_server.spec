# -*- mode: python -*-
a = Analysis(['start_server.py'],
             pathex=['/home/thorax/Documents/dev/hackathon/bitcoin2015/poc/bitwave/bitwave'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='start_server',
          debug=False,
          strip=None,
          upx=True,
          console=True )
