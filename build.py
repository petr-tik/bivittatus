from distutils.core import setup, Extension


setup(ext_modules=[Extension("toymod", ["ext.c"])])
