#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8 ff=unix ft=python
"""
@author: Wu Liang
@contact: garcia.relax@gmail.com
@date: 2015/05/10
"""

import os
import shutil
from setuptools import setup
from setuptools import Command
from setuptools import find_packages

version = '0.1.1'

class CleanCommand(Command):
    description = "clean build directories"
    user_options = []
    def initialize_options(self):
        self.cwd = None
    def finalize_options(self):
        self.cwd = os.getcwd()
    def run(self):
        if os.path.exists(os.path.join(os.path.dirname(__file__), "build")):
            shutil.rmtree(os.path.join(os.path.dirname(__file__), "build"))
        if os.path.exists(os.path.join(os.path.dirname(__file__), "dist")):
            shutil.rmtree(os.path.join(os.path.dirname(__file__), "dist"))
        if os.path.exists(os.path.join(os.path.dirname(__file__), "nodechalk.egg-info")):
            shutil.rmtree(os.path.join(os.path.dirname(__file__), "nodechalk.egg-info"))

setup(name = 'nodechalk',
    version = version,
    description = "Terminal string styling for python",
    long_description = "",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: Freely Distributable",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: Chinese (Simplified)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.4",
        "Topic :: Utilities",
    ],
    keywords = ("chalk", "terminal color"),
    author = 'magicsky',
    author_email = 'garcia.relax@gmail.com',
    url = 'https://github.com/magicsky/nodechalk',
    license = 'MIT',
    packages = find_packages(),

    cmdclass = {
        "clean": CleanCommand
    }
)

