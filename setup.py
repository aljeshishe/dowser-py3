#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: setup.py
Version: 0.1
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2015-11-24
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
f = path.join(here, 'README.md')

try:
    from pypandoc import convert
    long_description = convert(f, 'rst')
except ImportError:
    print(
        "pypandoc module not found, could not convert Markdown to RST")
    long_description = open(f, 'r').read()

setup(
    name='dowser-py3',
    version='0.2.2',
    description="Python3 fork of dowser library",
    long_description=long_description,
    url='https://github.com/appknox/dowser-py3',
    author='dhilipsiva',
    author_email='dhilipsiva@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='dowser memory leak',
    packages=find_packages(),
    py_modules=['dowser'],
    package_data={'dowser': ['*.html', '*.css']},
    entry_points='''
    ''',
    install_requires=[
        'CherryPy',
        'emport',
        'infi.pyutils',
        'infi.recipe.console-scripts',
        'Logbook',
        'packaging',
        'pbr',
        'Pillow',
        'z3c.recipe.scripts',
        'zc.buildout',
        'zc.recipe.egg',
    ],
    extras_require={
        'dev': [''],
        'test': [''],
    },
)
