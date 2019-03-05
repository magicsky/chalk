#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8 ff=unix ft=python
"""
@author: Wu Liang
@contact: garcia.relax@gmail.com
@date: 2015/05/09
"""

from __future__ import absolute_import

import os
import re
import sys

def getIsTermSupport():
    pattern = re.compile("^screen|^xterm|^vt100|color|ansi|cygwin|linux", re.IGNORECASE)
    return pattern.match(os.getenv("TERM")) is not None

def isSupportColor():
    return (os.isatty(sys.stdout.fileno()) != 0 and getIsTermSupport()) and \
        (os.isatty(sys.stderr.fileno()) != 0 and getIsTermSupport())
