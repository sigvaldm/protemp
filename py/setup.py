#!/usr/bin/env python
"""
Copyright {year} {author} <{email}>

This file is part of {project}.

{project} is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

{project} is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with {project}  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup
from io import open # Necessary for Python 2.7

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(name='{project}',
      version='0.1.0',
      description='{desc}',
      long_description=long_description,
      author='{author}',
      author_email='marholm@marebakken.com',
      url='https://github.com/sigvaldm/{project}.git',
      py_modules=['{project}'],
      license='LGPL',
      classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        ]
     )

