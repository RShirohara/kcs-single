#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Shiro_Shz

import os
import random
import sys

args = sys.argv[1]

with open("Novel/kcs/Single/data/03/selected21_shigure.dat", 'r') as _file:
    _dat = _file.readlines()

for _cnt in range(int(args)):
    _loadcnt = random.randint(0, len(_dat))
    print(_dat[_loadcnt].replace("\n", ""))
