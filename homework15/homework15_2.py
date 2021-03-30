# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:16:04 2021

@author: Fenrir

Description :


"""
# list and in
input_line = input()
list_char = ['A', 'E', 'G', 'I', 'O', 'S', 'Z']
list_number = [4, 3, 6, 1, 0, 5, 2]

for c in input_line:
    if c in list_char:
        print(list_number[list_char.index(c)], end = "") 
    else: 
        print(c, end = "")
        

"""
# if else
input_line = input()
for c in input_line:
    if c == 'A':
        print('4', end = "") 
    elif c == 'E':
        print("3", end = "") 
    elif c == 'G':
        print("6", end = "") 
    elif c == 'I':
        print("1", end = "") 
    elif c == 'O':
        print("0", end = "") 
    elif c == 'S':
        print("5", end = "") 
    elif c == 'Z':
        print("2", end = "") 
    else:
        print(c, end = "")   

# function and map
def Leet_fun(c):
    list_char = ['A', 'E', 'G', 'I', 'O', 'S', 'Z']
    list_number = [4, 3, 6, 1, 0, 5, 2]
    if c in list_char:
        return str(list_number[list_char.index(c)])
    else: 
        return c
input_line = input()

ans_str = ''.join(list(map(Leet_fun, input_line))) 

print(ans_str)

"""