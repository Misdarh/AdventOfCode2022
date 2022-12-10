#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:41:19 2022

@author: jeff
"""
import numpy as np
day='6'
path_file = "/home/jeff/Bureau/AdventOfCode2022/AdventOfCode2022/Day_0"+day+"/input_0"+day+".txt"

file = open(path_file, "r")
lines = file.readlines()

code = lines[0]
#code="nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
k=0
while k<len(code):
  if code[k]!=code[k+1] and code[k]!=code[k+2] and code[k+1]!=code[k+2]: #3différents
    if code[k+3]!=code[k] and code[k+3]!=code[k+1] and code[k+3]!=code[k+2]:
      print('FINI')
      print(k+4)
      k=len(code)+1
    else:
      k+=1
  else:
    k+=1
    

k=0
kmax=len(code)
while k<kmax:
  
  message=code[k:k+14]
  list_i = [message.count(letter) for letter in message]
  if np.prod(list_i)==1:
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print(k+14)
    k=kmax+1
  else:
    k+=1
