
a = Analysis(...)
pyz = PYZ(a.pure)
pkg = PKG(a.pure, name="PackageName")
exe = EXE(pyz, pkg,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          ...)