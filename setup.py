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

    # at the moment deps are managed solely via conda
    install_requires=[],
    tests_require=[],
    extras_require={},

    entry_points={
        'console_scripts': [
            'frankenbody = frankenbody.commands:main'
        ]
    },

    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    platforms=['Any'],
)
