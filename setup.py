#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='wcst_latents',
    version='0.0.0',
    description='Making hierarchical_lfads repo pip installable',
    author='Patrick Zhang',
    author_email='pqz317@uw.edu',
    packages=find_packages(exclude=[]),
)

