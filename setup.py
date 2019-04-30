#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

from setuptools import setup
from setuptools import find_packages

def get_version(*file_paths):
    """Retrieves the version from csv2json-timelinejs/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

version = get_version("csv2json_timelinejs", "__init__.py")
readme = open('README.md').read()

requirements = []

setup(
    name='csv2json_timelinejs',
    version=version,
    description=""" Turns CSV file to JSON that can be used in TimelineJS """,
    long_description=readme,
    author='lduarte1991',
    author_email='luis_duarte@harvard.edu',
    url='https://github.com/lduarte1991/csv2json-timelinejs',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'csv2json_timelinejs=csv2json_timelinejs.csv_to_timelinejs_json:main'
        ]
    },
    package_data={},
    install_requires=requirements,
    zip_safe=False,
    keywords='timelinejs csv csv2json csvjson-timelinejs csv_to_timelinejs_json',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
