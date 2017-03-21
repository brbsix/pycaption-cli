# -*- coding: utf-8 -*-
"""Application setup script"""

import os
from setuptools import setup, find_packages


def read(path):
    """Return file contents."""
    with open(path) as file_object:
        return file_object.read()


# allow setup.py to be run from any path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

setup(
    name='pycaption-cli',
    version='0.1',
    description='Command line caption conversion',
    long_description=read('README.md'),
    author='Joe Norton',
    author_email='joey@nortoncrew.com',
    url='https://github.com/jnorton001/pycaption-cli',
    install_requires=['pycaption'],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['pycaption=pycapcli.caption_converter:main'],
    }
)
