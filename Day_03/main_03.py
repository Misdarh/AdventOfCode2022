#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:41:19 2022

@author: jeff
"""

path_file = "/home/jeff/Bureau/AdventOfCode2022/AdventOfCode2022/Day_03/input_03.txt"

file = open(path_file, "r")
lines = file.readlines()

total=0
shift=ord('a')-1
for line in lines:

  line_s=line.strip()

  first = line_s[:int(len(line_s)/2)]
  second = line_s[int(len(line_s)/2):]
  common_letter = list(set(first).intersection(second))[0]

  total+= ord(common_letter.lower())-shift+26*(1-int(common_letter.lower()==common_letter))
  
print(total)

k=0
total=0

while k<len(lines)-2:
  line0=lines[k].strip()
  line1=lines[k+1].strip()
  line2=lines[k+2].strip()
  common_letter0 = list(set(line0).intersection(line1))
  common_letter1 = list(set(line0).intersection(line2))
  common_letter2 = list(set(line1).intersection(line2))
  
  common_letter=list(set(common_letter0).intersection(set(common_letter1).intersection(common_letter2)))[0]

  total+= ord(common_letter.lower())-shift+26*(1-int(common_letter.lower()==common_letter))
  k+=3
  
print(total)
