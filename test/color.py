#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8 ff=unix ft=python
"""
@author: Wu Liang
@contact: garcia.relax@gmail.com
@date 2015-05-09 23:29
"""

import os
import sys

currentPath = os.path.normpath(os.path.dirname(os.path.realpath(__file__)))
rootPath = os.path.normpath(os.path.dirname(currentPath))
sys.path.insert(0, rootPath)

import chalk

print "%s %s %s %s %s %s %s" % (
    chalk.bold("bold"),
    chalk.dim("dim"),
    chalk.italic("italic"),
    chalk.underline("underline"),
    chalk.inverse("inverse"),
    chalk.strikethrough("strikethrough"),
    chalk.black(chalk.gray("black")),
)
print "%s %s %s %s %s %s %s %s" % (
    chalk.red("red"),
    chalk.green("green"),
    chalk.yellow("yellow"),
    chalk.blue("blue"),
    chalk.magenta("magenta"),
    chalk.cyan("cyan"),
    chalk.white("white"),
    chalk.gray("gray")
)
print "%s %s %s %s %s %s %s" % (
    chalk.bgRed("bgRed"),
    chalk.bgGreen("bgGreen"),
    chalk.bgYellow("bgYellow"),
    chalk.bgBlue("bgBlue"),
    chalk.bgMagenta("bgMagenta"),
    chalk.bgCyan("bgCyan"),
    chalk.bgWhite("bgWhite")
)

