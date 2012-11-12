#!/usr/bin/env python
""" Setup file for yandexweather package """

from distutils.core import setup
from os.path import abspath, dirname, join

dir=dirname(abspath(__file__))
description = open(join(dir,'description')).read()
readme = open(join(dir,'README.rst')).read()

setup(name='yandexweather',
      version='0.0.2',
      description=description,
      long_description=readme,
      author='cancerhermit',
      author_email='cancerhermit@gmail.com',
      url='http://github.com/cancerhermit/PyYandexWeather/',
      install_requires=[
        'lxml'
      ],
      packages = ["yandexweather"],
      classifiers=(
          'Environment :: Console',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
        ),
      license="GPL"
     )