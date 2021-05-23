# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 16:42:16 2021

@author: Fenrir

"""

import random

n = int(input("Input n: "))
random_list = []

for i in range(n):
    r_l = random.randint(1, 100)
    random_list.append(r_l)
print("Original:",random_list)

print("Result:", sorted(random_list)[1:-1])

"""
random_list.sort()
print("Result:", random_list[1:-1])
"""
