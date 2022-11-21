# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:55:31 2022

@author: compro
"""

for j in range(2,21):
    for i  in range(2,j):
        if j%i==0:
            print(f"{j} is not a prime number")
            break
    else:
        print(f"{j} is a prime number")