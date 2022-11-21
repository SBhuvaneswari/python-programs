# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:04:51 2022

@author: compro
"""

a=0
b=1
#0,1,1,2,3,5,8....
fib=[0,1]
number=int(input("enter the number"))
if number==0:
    print(a)
if number==1:
    print(b)
for i in range(2,number+1):
    c=a+b
    a=b
    b=c
    fib.append(b)
print(b)
print(fib)
