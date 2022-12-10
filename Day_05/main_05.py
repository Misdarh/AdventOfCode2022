#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:41:19 2022

@author: jeff
"""
import numpy as np
day='5'
path_file = "/home/jeff/Bureau/AdventOfCode2022/AdventOfCode2022/Day_0"+day+"/input_0"+day+".txt"

file = open(path_file, "r")
lines = file.readlines()

def ajoute_elem_liste(elt,l):
   
  k=1
  while k<len(l):
    print(k, l[k])
    if l[k]!="":
      l[k-1]=elt
      return l
    k+=1
  
def find_premier_elem(l):
  k=0
  while k<len(l):
    if l[k]!="":
      return l[k], k
    k+=1
  print("hum :", l)
  return ""


def find_list(orig, dest):
  
  if orig=="1":
    li_orig=list_1
  elif orig=="2":
    li_orig=list_2
  elif orig=="3":
    li_orig=list_3
  elif orig=="4":
    li_orig=list_4
  elif orig=="5":
    li_orig=list_5
  elif orig=="6":
    li_orig=list_6
  elif orig=="7":
    li_orig=list_7
  elif orig=="8":
    li_orig=list_8
  elif orig=="9":
    li_orig=list_9
  else:
    print("problème orig:", orig)

  if dest=="1":
    li_dest=list_1
  elif dest=="2":
    li_dest=list_2
  elif dest=="3":
    li_dest=list_3
  elif dest=="4":
    li_dest=list_4
  elif dest=="5":
    li_dest=list_5
  elif dest=="6":
    li_dest=list_6
  elif dest=="7":
    li_dest=list_7
  elif dest=="8":
    li_dest=list_8
  elif dest=="9":
    li_dest=list_9
  else:
    print("problème dest:", dest)
  
  
  return li_orig, li_dest
    
    
  

list_1=["","","R","Q","G","P","C","F"]
list_2=["","","","","P","C","T","W"]
list_3=["","","","C","M","P","H","B"]
list_4=["","R","P","M","S","Q","T","L"]
list_5=["","N","G","V","Z","J","H","P"]
list_6=["","","","","","J","P","D"]
list_7=["R","T","J","F","Z","P","G","L"]
list_8=["J","T","P","F","C","H","L","N"]
list_9=["W","C","T","H","Q","Z","V","G"]

#k=10 #10
#kmax=len(lines)
#while k<kmax:
#  line_s=lines[k].strip().split('from')
#  line_s[0].strip().split("move")
#  line_s[1].strip().split("to")
#  tot=int(line_s[0].strip().split("move")[1].strip())
#  orig=line_s[1].strip().split("to")[0].strip()
#  dest=line_s[1].strip().split("to")[1].strip()
#  li_orig, li_dest = find_list(orig,dest)
#  print(tot,orig,dest)
#  print(li_orig)
#  print(li_dest)
#  qte=0
#  if k==16 :
#    print("*******************************************")
#  while qte<tot:
#    elt, idx = find_premier_elem(li_orig)
#    print(elt)
#    print(li_dest)
#    if li_dest[0]!="":
#      li_dest.insert(0,elt)
#    elif li_dest[-1]=="":
#      li_dest[-1]=elt
#    else:
#      li_dest = ajoute_elem_liste(elt,li_dest)
#    print(idx)
#    li_orig[idx]=""
#    print(li_orig)
#    print(li_dest)
#    qte+=1
#  
#  
#  k+=1
  
print(find_premier_elem(list_1))
print(find_premier_elem(list_2))
print(find_premier_elem(list_3))
print(find_premier_elem(list_4))
print(find_premier_elem(list_5))
print(find_premier_elem(list_6))
print(find_premier_elem(list_7))
print(find_premier_elem(list_8))
print(find_premier_elem(list_9))

print("********************************************")

k=10 #10
kmax=len(lines)
while k<kmax:
  line_s=lines[k].strip().split('from')
  line_s[0].strip().split("move")
  line_s[1].strip().split("to")
  tot=int(line_s[0].strip().split("move")[1].strip())
  orig=line_s[1].strip().split("to")[0].strip()
  dest=line_s[1].strip().split("to")[1].strip()
  li_orig, li_dest = find_list(orig,dest)
  print(tot,orig,dest)
  print(li_orig)
  print(li_dest)
  qte=0
  list_aux=[]
  while qte<tot:
    elt, idx = find_premier_elem(li_orig)
    print(elt, idx)
    print(li_dest)
    list_aux.insert(0,elt)
    li_orig[idx]=""
    qte+=1
  
  
  for ll in list_aux:
    
    if li_dest[0]!="":
      li_dest.insert(0,ll)
    elif li_dest[-1]=="":
      li_dest[-1]=ll
    else:
      li_dest = ajoute_elem_liste(ll,li_dest)
  print("ùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùù")
  print(li_orig)
  print(li_dest)

  k+=1
  
print(find_premier_elem(list_1))
print(find_premier_elem(list_2))
print(find_premier_elem(list_3))
print(find_premier_elem(list_4))
print(find_premier_elem(list_5))
print(find_premier_elem(list_6))
print(find_premier_elem(list_7))
print(find_premier_elem(list_8))
print(find_premier_elem(list_9))