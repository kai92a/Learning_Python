# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 02:35:26 2021

@author: sgaa_
"""

print ('Hello World')
a = input('Enter a number or any string')
print (type (a))
a = int (a)
print ("a is now int")
print (type (a))
a = float (a)
print ("a is now a float")
print (type (a))
b = input ('enter 1 or 0 or True or false')
print (b)
print (type(b))
print ("Now converting to bool")
b= bool(int (b))
print (type (b))
print (b)
c = int (input ("enter a value for  c:"))
d = int (input ("enter a value for d:"))
print ("adding c and d: ")
print (c+d)
print ("multiplying c and d: ")
print (c*d)
print ("subtracting c from d: ")
print (d-c)
print ("modulo of c and d: ")
print (d%c)
print ("d divided by c: " )
print (d/c)
print ("int part of d divided by c: ")
print (d//c)





