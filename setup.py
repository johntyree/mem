#!/usr/bin/env python

from distutils.core import setup

setup(name='Mem',
      version='1.0',
      description='The mem (memoize) build system',
      author='Scott R Parish',
      author_email='srp@srparish.net',
      packages=['mem',
                'mem.tasks',
                'mem.nodes'],
      scripts=['script/mem'],
     )