#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:41:19 2022

@author: jeff
"""

path_file = "/home/jeff/Bureau/AdventOfCode2022/AdventOfCode2022/Day_04/input_04.txt"

file = open(path_file, "r")
lines = file.readlines()

total=0
shift=ord('a')-1
for line in lines:

  line_s=line.strip().split(',')

  min1=int(line_s[0].split('-')[0])
  max1=int(line_s[0].split('-')[1])

  min2=int(line_s[1].split('-')[0])
  max2=int(line_s[1].split('-')[1])
  
#  print(min1, max1)
#  print(min2, max2)
  
  if (min2>=min1 and max2<=max1) or (min1>=min2 and max1<=max2):
    total+=1

print(total)

total=0
import numpy as np
for line in lines:

  line_s=line.strip().split(',')

  min1=int(line_s[0].split('-')[0])
  max1=int(line_s[0].split('-')[1])

  min2=int(line_s[1].split('-')[0])
  max2=int(line_s[1].split('-')[1])
  
  seg1=[str(i) for i in np.arange(min1,max1+1)]
  seg2=[str(i) for i in np.arange(min2,max2+1)]
  
 # print(seg1)
 # print(seg2)
  
  if len(set(seg1).intersection(seg2))>0:
    total+=1
  
print(total)