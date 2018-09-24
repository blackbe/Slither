# -*- mode: python -*-
a = Analysis(['slither.py'],
         pathex=['C:\\Users\\Ben Black\\PycharmProjects\\slither\\slither'],
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('snakehead.png','C:\\Users\\Ben Black\\PycharmProjects\\slither\\slither\\snakehead.png', 'Data'),('apple.png','C:\\Users\\Ben Black\\PycharmProjects\\slither\\slither\\apple.png', 'Data'), ('icon.png','C:\\Users\\Ben Black\\PycharmProjects\\slither\\slither\\icon.png', 'Data')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='slither.exe',
      debug=False,
      strip=None,
      upx=True,
      console=True, icon='C:\\Users\\Ben Black\\PycharmProjects\\slither\\slither\\icon_FaU_icon.ico')