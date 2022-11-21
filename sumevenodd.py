# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:43:01 2022

@author: compro
"""

sum_of_even=0
sum_of_odd=0
for number in range(1,11,1):
    if number%2==0:
        sum_of_even+=number   
    else:
        sum_of_odd+=number
print(f"sum of even = {sum_of_even}")
print(f"sum of odd = {sum_of_odd}")