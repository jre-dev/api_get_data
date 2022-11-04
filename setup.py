#!/usr/bin/env python

from setuptools import setup, find_packages
from src.main import __version__

setup(
    name='api_get_data',
    version=__version__,
    author='Jonathan Reinhardt',
    packages=find_packages(),
)
