#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:41:19 2022

@author: jeff
"""

path_file = "/home/jeff/Bureau/AdventOfCode2022/Day_02/input_02.txt"

file = open(path_file, "r")
lines = file.readlines()

total=0
for line in lines:
  opp = line[0]
  me = line[2]
  
  if opp=="A":
    if me=="X":
      total+=1+3
    elif me=="Y":
      total+=2+6
    else: #Z
      total+=3+0
  elif opp=="B":
    if me=="X":
      total+=1+0
    elif me=="Y":
      total+=2+3      
    else: #Z
      total+=3+6    
  else: #C
    if me=="X":
      total+=1+6
    elif me=="Y":
      total+=2+0
    else:#Z
      total+=3+3

print("max total : ", total)

total=0
for line in lines:
  opp = line[0]
  res = line[2]
  
  if opp=="A":
    if res=="X":
      total+=3+0
    elif res=="Y":
      total+=1+3
    else: #Z
      total+=2+6
  elif opp=="B":
    if res=="X":
      total+=1+0
    elif res=="Y":
      total+=2+3
    else: #Z
      total+=3+6
  elif opp=="C":
    if res=="X":
      total+=2+0
    elif res=="Y":
      total+=3+3
    else: #Z
      total+=1+6


print("optim total : ", total)
