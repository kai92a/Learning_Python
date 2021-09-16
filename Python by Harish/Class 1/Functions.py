# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 05:53:18 2021

@author: sgaa_
"""
#Addition of two numbers
a=int (input ("enter a: "))
b=int (input ("enter b: "))

def F_add(x,y):
    global c
    c=x+y
    return(c)

d= F_add(a,b)
print (d)
print (c)

def F_sub(x,y):
    c=x-y
    return (c)




