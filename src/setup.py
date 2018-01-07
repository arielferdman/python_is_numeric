#!/usr/bin/env python3
# encoding: utf-8

from distutils.core import setup, Extension

strextnd_module = Extension('strextnd', sources = ['strextnd.c'])

setup(name='strextnd',
      version='0.1.0',
      description='Module written in C that extends the python3 str library',
      ext_modules=[strextnd_module])
