# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 21:51:08 2021

@author: Fenrir

"""
h = int(input("縦方向のマス数:"))
w = int(input("横方向のマス数:"))
n = int(input("移動数:"))
move_direction = ['U', 'D', 'L', 'R']
move_x = [1, -1, 0, 0]
move_y = [0, 0, -1, 1]

y = 0
x = 0

for i in range(n):
    op = input()
    move_index = move_direction.index(op)
    x += move_x[move_index]
    y += move_y[move_index]
    #print(x, y)
if 0 <= x < w and 0 <= y < h:
    print("valid")
else:
    print("invalid")  
    
""" 
# dictの方法
move = {'U':(1, 0), 'D':(-1, 0), 'L':(0, -1), 'R':(0, 1)} 
y, x = 0, 0

for i in range(n):
    op = input()
    move_x, move_y = move[op]
    x += move_x
    y += move_y 
"""  
