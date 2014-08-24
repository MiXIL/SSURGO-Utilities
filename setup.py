#!/usr/bin/env python

from distutils.core import setup

setup(name='SSURGO-Utilities',
      description = 'Utility scipts for working with SSURGO data as a Raster Attribute Table',
      author = 'Daniel Clewley',
      author_email = 'daniel.clewley@gmail.com',
      url = 'http://mixil.usc.edu/',
      scripts=['convertSSURGO2RAT.py'],
      py_modules=['ssurgofields'])
