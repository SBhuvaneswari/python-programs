# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:21:42 2022

@author: Bhuvaneswari Sivagnanam
"""
for i in range(11):
    year = int(input("Enter the year: "))
    if year%100 == 0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        if year%4 == 0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")