# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:28:36 2021

@author: Fenrir

Description :

Variable:
    
Algorithm/Calculation:
"""

# 1
birthday = ["19930911", "20010621", "19801110", "19980507", "20100101"]
year = [x[:4] + "年" for x in birthday]
month = [x[4:6]  + "月"for x in birthday]
day = [x[6:] + "日" for x in birthday]
print("Year List:", year)
print("Month List:", month)
print("Day List:", day)