# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:42:16 2021

@author: Fenrir

"""

s = input("please enter string: ")

suffix = input("Please enter the suffix you want to judge: ")

if s[-len(suffix):] == suffix:
    print("True")

else:
    print("False")


