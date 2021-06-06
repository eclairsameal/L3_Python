# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:28:36 2021

@author: Fenrir

Description :

Variable:
    
Algorithm/Calculation:
"""
birthday = ["19930911", "20010621", "19801110", "19980507", "20100101", "20090519", "20140712", "20110323", "19990415", "20001224"]
year = [x[:4] for x in birthday if int(x[:4]) >= 2000]
month = ["7~12" if int(x[4:6]) >= 7 else "1~6" for x in birthday]
print(year)
print(month)






