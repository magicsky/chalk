#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8 ff=unix ft=python
"""
@author: Wu Liang
@contact: garcia.relax@gmail.com
@date: 2015/05/09
"""

from types import ModuleType
import os
import re
import sys

from SupportedColor import isSupportColor

class Chalk(ModuleType):

    def __init__(self, selfModule):
        self.selfModule = selfModule
        self.styles = {
            "modifiers": {
                "reset": [0, 0],
                "bold": [1, 22], # 21 isn't widely supported and 22 does the same thing
                "dim": [2, 22],
                "italic": [3, 23],
                "underline": [4, 24],
                "inverse": [7, 27],
                "hidden": [8, 28],
                "strikethrough": [9, 29]
            },
            "colors": {
                "black": [30, 39],
                "red": [31, 39],
                "green": [32, 39],
                "yellow": [33, 39],
                "blue": [34, 39],
                "magenta": [35, 39],
                "cyan": [36, 39],
                "white": [37, 39],
                "gray": [90, 39]
            },
            "bgColors": {
                "bgBlack": [40, 49],
                "bgRed": [41, 49],
                "bgGreen": [42, 49],
                "bgYellow": [43, 49],
                "bgBlue": [44, 49],
                "bgMagenta": [45, 49],
                "bgCyan": [46, 49],
                "bgWhite": [47, 49]
            }
        }

    def __getattr__(self, style):
        def colorIt(s):
            found = None
            colored = s
            for key, value in self.styles.iteritems():
                for name, values in value.iteritems():
                    if name != style:
                        continue
                    found = values
            if isSupportColor() and found is not None:
                colored = str(u'\u001b[') + str(found[0]) + "m" + s + str(u'\u001b[') + str(found[1]) + "m"
            return colored
        return colorIt

self = sys.modules[__name__]
sys.modules[__name__] = Chalk(self)


