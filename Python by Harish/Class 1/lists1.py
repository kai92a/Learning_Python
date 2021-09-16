# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 04:40:55 2021

@author: sgaa_
"""
a_str=input ("enter the characters for the list")
a_str=list(a_str)
i=len(a_str)
print (i)
j=0
while j<i:
    k=j+2
    a_str2=a_str[j:k]
    if len(a_str2)>=2:
        print (a_str2)
    j+=1