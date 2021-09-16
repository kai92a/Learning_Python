# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 03:52:33 2021

@author: sgaa_
"""

a = "12345"
a = list (a)
i=0
while i < len(a):
    a[i]=int (a[i])
    i+=1
print (a)
print (type (a[1]))

