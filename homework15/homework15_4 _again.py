# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:18:44 2021

@author: Fenrir

Description :
    2つの数値aとbをユーザーに入力させ、a~bの整数値で要素が重複しないListを作成する。
    前述のListを使用しユーザーとコンピューターが数字比較を行うゲームを作ってください。

    1.ユーザーが数字の位置を選びます
    2.コンピューターが数字の位置を選びます
    3.双方の数字を比較し、大きかった方が勝利し、両方の数値を加算しポイントとする
    4.1～3を続けて、Listの選ばれていない要素が残り1つ又はなくなるまで続ける
    5.ポイントの高い方を勝者とし出力する
"""
import random

def rand_ab(a, b):
    """重複しない乱数(range: a ~ b)"""
    list_a = []
    for i in range(b - a + 1):
        random_var = random.randint(a, b)
        while random_var in list_a: # もし重複したら、もう一度乱数を生成します。
            random_var = random.randint(a, b)
        list_a.append(random_var) # 乱数の範囲は1～9
    return list_a

def print_list_interface(l, pick_flag):
    """選択したインターフェース"""
    for i in range(len(pick_flag)):
        if pick_flag[i] == 0:
            print("*", end = " ")
        else:
            print(l[i], end = " ")
    print("")
    
def player_pick(l, pick_flag):
    pick = int(input("choose one:"))
    while pick_flag[pick] != 0 : # もし重複したら、もう一度選択してください
        pick = int(input("Choose again:"))
    pick_flag[pick] = 1 # 選択した場所にマークを付ける
    return l[pick] # 選択した番号

def computer_pick(l, pick_flag):
    pick = random.randrange(len(pick_flag))
    while pick_flag[pick] !=0 :  # もし重複したら、もう一度乱数を生成します。
        pick = random.randrange(len(pick_flag))
    pick_flag[pick] = 1  # 選択した場所にマークを付ける  
    return l[pick]

def comparison_size(p, c, p_point, c_point):
    """誰がポイントを獲得するかを比較する"""
    if p >= c:
        p_point+=p + c
        print("The player wins {} points.".format(p_point))
    else:
        c_point+=p + c
        print("The computer wins {} points.".format(c_point))
    return p_point, c_point

def game():
    list_a = [] # a~bの整数値で要素が重複しないList
    list_a_pick_flag = [] # 選ばれたことはありますか
    a = int(input("input a:"))
    b = int(input("input b:"))
    list_a = rand_ab(a, b)
    # print(list_a)
    list_a_pick_flag = [0] * (b - a + 1)
    print_list_interface(list_a.copy(), list_a_pick_flag.copy())
    
    player_points = 0
    computer_points = 0
    while list_a_pick_flag.count(0) > 1: 
        player_pick_number = player_pick(list_a, list_a_pick_flag)
        computer_pick_number = computer_pick(list_a, list_a_pick_flag)
        print_list_interface(list_a.copy(), list_a_pick_flag.copy())
        print("Numbers selected by the computer: {}".format(player_pick_number))    
        print("Numbers selected by the player: {}".format(computer_pick_number)) 
        player_points, computer_points = comparison_size(player_pick_number, computer_pick_number, player_points, computer_points)
    print("------------------------end------------------------------------")
    print("The computer wins {} points.".format(computer_points))
    print("The player wins {} points.".format(player_points))
    if player_points >= computer_points:
        print("The player wins the game.")
    else:
        print("The computer wins the game.")

def main():    
    while True :
        game()
        ans = input("Whether to play again(Y/N):")
        if ans == "n" or ans == "N":
            break

main()