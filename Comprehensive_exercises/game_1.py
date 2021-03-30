# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 09:23:46 2021

@author: Fenrir

Description :

Variable:
    
Algorithm/Calculation:
    Two to one dimension: fun(x, y) = (x - 1) * n + (y - 1)
"""
import random

# function
def new_card_list(n):
    """Initialize the card list"""
    temp_list = [x for x in range(1, int((n * n)/2) + 1)]
    temp_list.extend(temp_list.copy())
    if (n * n)%2 != 0: # Add a ghost card(0) if the number is odd
        temp_list.append(0)
    # print(temp_list)
    return temp_list

def shuffle(list_a):
    """Shuffle the list_a"""
    for i in range(len(list_a)): # 理論上では半分以上並び替えればかなり要素を乱せます。
        random_index = random.randrange(len(list_a)) # 乱数で要素を交換する位置を生成します。
        list_a[i], list_a[random_index] = list_a[random_index], list_a[i]
    #print(list_a)
    
def card_interface(card, flag, n):
    """Print the flop interface"""
    print("-" * (n*3 + 1))
    for i in range(1, n+1):
        print("|", end = "")
        for j in range(1, n+1):
            l_index = (i -1) * n + (j - 1)
            if flag[l_index] == 0:
                print("{0:>2}".format("*"), end = "|")
            else:
                if card[l_index] == 0:
                    print("{0:>2}".format("J"), end = "|")
                else:
                    print("{0:>2}".format(card[l_index]), end = "|")
        print()
        print("-" * (n*3 + 1))
        
def cal_position(s, n):
    """Cut and calculate the entered value"""
    x1, y1, x2, y2 = list(map(int, s.split()))
    # print(x1, y1, x2, y2) 
    while x1 == x2 and y1 == y2: # Enter the same value(fool-proof)
        s = input("Please choose 2 places again(The input is the same): ")
        x1, y1, x2, y2 = list(map(int, s.split()))
    while not in_range(n, x1, y1, x2, y2):
        s = input("Please choose 2 places again(Out of range): ")
        x1, y1, x2, y2 = list(map(int, s.split()))        
    pick_position1 = pick_position_fun(x1, y1, n)
    pick_position2 = pick_position_fun(x2, y2, n)
    # print(pick_number1, pick_number2)
    return pick_position1, pick_position2

def in_range(n, x1, y1, x2, y2):
    if 0 < x1 <= n and 0 < x2 <= n and 0 < y1 <= n and 0 < y2 <= n:
        return True
    else:
        return False
    

def flag_control(flag_list, switch_open, *f_index):
    """Control list flag(If switch_open = True, it is open, if switch_open = False, it is closed)"""
    if switch_open:
        for i in f_index:
            flag_list[i] = 1
    else:
        for i in f_index:
            flag_list[i] = 0        

def pick_position_fun(x, y, n):
    """Calculate the position from two-dimensional to one-dimensional"""
    return (x - 1) * n + (y - 1)   
   
def test_print_card(c, p, n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            l_index = (i -1) * n + (j - 1)
            print("{0:>2}".format(c[l_index]), end = " ")
        print()
    print(p)

def game():
    card_list = []
    pick_flag = []
    pair_count = 0
    game_point = 0
    n = int(input("Please enter the size of this matrix(1 ~ 9): "))
    while not(0 < n < 9):
        n = int(input("Please enter the size of this matrix again(1 ~ 9): "))
    card_list = new_card_list(n)
    pick_flag = [0 for x in range(len(card_list))]
    shuffle(card_list)
    test_print_card(card_list, pick_flag, n) # test
    print("----------------------------------------------------")
    card_interface(card_list, pick_flag, n) # interface
    # start
    if (n * n)%2 != 0:
        m = (n * n) -1
    else:
        m = (n * n)
    while pair_count < m:
        input_op = input("Please choose 2 places: ")
        pick_position1, pick_position2 = cal_position(input_op, n)
        while pick_flag[pick_position1] == 1 or pick_flag[pick_position2] == 1:
            input_op = input("Please choose 2 places again(Has been turned over): ")
            pick_position1, pick_position2 = cal_position(input_op, n)
        # print(pick_position1, pick_position2)
        flag_control( pick_flag, True, pick_position1, pick_position2)
        card_interface(card_list, pick_flag, n) # interface
        if card_list[pick_position1] == card_list[pick_position2]:
            game_point += 10
            print("---------- Pair(Game points: {}) ----------".format(game_point))
            pair_count += 2
        else:
            flag_control( pick_flag, False, pick_position1, pick_position2)
            game_point -= 5
            print("---------- Not Pair(Game points: {})----------".format(game_point))
            card_interface(card_list, pick_flag, n) # interface
    print("Congratulations on clearing the game")
    print("Final game points: {}".format(game_point))
def main():

    game()
    
main()