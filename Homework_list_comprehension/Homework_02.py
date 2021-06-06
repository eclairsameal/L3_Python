# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:28:36 2021

@author: Fenrir

Description :

Variable:
    
Algorithm/Calculation:
"""

s = input("input string:").split()  # python algorithm java android google
# print(s)
select_index = []
for i in range(len(s)):
    n = int(input("Select a character in the {}: ".format(s[i])))
    while n >= len(s[i]) or n < 0:
        n = int(input("Enter again: "))
    select_index.append(n)
#print(select_index)

select_char = [s[i][select_index[i]] for i in range(len(s)) ]
print("Selected character elements:", select_char)