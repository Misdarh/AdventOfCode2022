#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:54:10 2022

@author: jeff
"""

path_file = "/home/jeff/Bureau/AdventOfCode2022/Day_01/input.txt"

file = open(path_file, "r")
lines = file.readlines()

maxi=[]
line=0

while line<len(lines):
  compt=0
  while lines[line]!="\n":
    compt+=int(lines[line])
    line+=1
  line+=1
  maxi.append(compt)

sorted_max = sorted(maxi)
import numpy as np
print(np.sum(sorted_max[-3::]))