#!/usr/bin/env python
from setuptools import setup

# Minimal setup.py to allow devel install the package
# Please use conda to setup the environment

setup(
    name='frankenbody',
    version='1.0dev0',
    author='Santi Villalba',
    author_email='santiago.villalba@bayer.com',
    url='https://github.com/bayer-science-for-a-better-life/mlr-challenges-frankenbody',
    license=None,
    py_modules=['frankenbody'],
    install_requires=[],
    platforms=['all'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD-3-Clause',
        'Topic :: Software Development',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
