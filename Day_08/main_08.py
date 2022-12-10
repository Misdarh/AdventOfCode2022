#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:41:19 2022

@author: jeff
"""
import numpy as np
day='8'
path_file = "/home/jeff/Bureau/AdventOfCode2022/AdventOfCode2022/Day_0"+day+"/input_0"+day+".txt"

file = open(path_file, "r")
lines = file.readlines()

forest = np.zeros(shape=(99,99),dtype=int)

for k in range(len(lines)):
  for (idx,tree) in enumerate(list(lines[k].strip())):
    forest[k][idx] = tree 


def visible(li):

  h = li[0]
  li_lin_left = li[1]
  li_lin_right = li[2]
  li_col_up = li[3]
  li_col_below = li[4]
  
  if len(li_lin_left)==0:
    maxi_left=-1
  else:
    maxi_left=max(li_lin_left)
  
  if len(li_lin_right)==0:
    maxi_right=-1
  else:
    maxi_right=max(li_lin_right)

  if len(li_col_up)==0:
    maxi_up=-1
  else:
    maxi_up=max(li_col_up)

  if len(li_col_below)==0:
    maxi_below=-1
  else:
    maxi_below=max(li_col_below)
  
  if h>maxi_left or h>maxi_right or h>maxi_up or h>maxi_below:
    return 1
  
  return 0


inside = forest[1:-1,1:-1]
lii = list(map(visible,
               [(forest[i,j], forest[i,:j],forest[i,j+1:],forest[:i,j],forest[i+1:,j])
               for i in range(1,np.shape(forest)[0]-1) for j in range(1,np.shape(forest)[1]-1)]))
  
print("Inside visibles : ", np.sum(lii))
print("Total visibles : ", np.sum(lii)-4+2*len(forest[0,:])+2*len(forest[:,0]))

def count_trees(li):
  
  h = li[0]
  li_lin_left = li[1]
  li_lin_right = li[2]
  li_col_up = li[3]
  li_col_below = li[4]
  tott=1
  tot=0
  k=0
  while k<len(li_lin_left):
    if h>li_lin_left[k]:
      tot+=1
    else:
      tot+=1
#       On compte les arbres au delà du premier au moins aussi grand
#      l=1
#      while k+l<len(li_lin_left):
#        if li_lin_left[k+l]>li_lin_left[k+l-1]:
#          tot+=1
#          l+=1
#        else:
#          l=len(li_lin_left)+1-k
      k=len(li_lin_left)+1
    k+=1

  tott*=tot
  tot=0
  k=0
  while k<len(li_lin_right):
    if h>li_lin_right[k]:
      tot+=1
    else:
      tot+=1
#       On compte les arbres au delà du premier au moins aussi grand
#      l=1
#      while k+l<len(li_lin_right):
#        if li_lin_right[k+l]>li_lin_right[k+l-1]:
#          tot+=1
#          l+=1
#        else:
#          l=len(li_lin_right)+1-k
      k=len(li_lin_right)+1
    k+=1

  tott*=tot

  tot=0 
  k=0
  while k<len(li_col_up):
    if h>li_col_up[k]:
      tot+=1
    else:
      tot+=1
#       On compte les arbres au delà du premier au moins aussi grand      
#      l=1
#      while k+l<len(li_col_up):
#        if li_col_up[k+l]>li_col_up[k+l-1]:
#          tot+=1
#          l+=1
#        else:
#          l=len(li_col_up)+1-k
      k=len(li_col_up)+1
    k+=1
  tott*=tot

  tot=0  
  k=0
  while k<len(li_col_below):
    if h>li_col_below[k]:
      tot+=1
    else:
      tot+=1
#       On compte les arbres au delà du premier au moins aussi grand      
#      l=1
#      while k+l<len(li_col_below):
#        if li_col_below[k+l]>li_col_below[k+l-1]:
#          tot+=1
#          l+=1
#        else:
#          l=len(li_col_below)+1-k
      k=len(li_col_below)+1
    k+=1
  tott*=tot

  return tott

cii = list(map(count_trees,
               [(forest[i,j], forest[i,:j][::-1],forest[i,j+1:],forest[:i,j][::-1],forest[i+1:,j])
               for i in range(1,np.shape(forest)[0]-1) for j in range(1,np.shape(forest)[1]-1)]))
  
  
  
print("Max trees : ", max(cii))