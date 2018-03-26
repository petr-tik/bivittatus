#!/usr/bin/env python3

from distutils.core import setup, Extension
import os

#os.environ["CC"] = "clang-3.7"


setup(ext_modules=[Extension("ctrie", ["trie.c"],
                             extra_compile_args=["-O3"])])
