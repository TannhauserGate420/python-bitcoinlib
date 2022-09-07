#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

from litecoin import __version__

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = []

setup(name='python-litecoinlib',
      version=__version__,
      description='The Swiss Army Knife of the Litecoin protocol.',
      long_description=README,
      long_description_content_type='text/markdown',
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
      ],
      url='https://github.com/tannhausergate420/python-litecoinlib',
      keywords='litecoin',
      packages=find_packages(),
      zip_safe=False,
      install_requires=requires
)
