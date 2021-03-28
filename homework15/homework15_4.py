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
list_a = [] # a~bの整数値で要素が重複しないList
list_a_pick_flag = [] # 選ばれたことはありますか
a = int(input("input a:"))
b = int(input("input b:"))
for i in range(b - a + 1):
    random_var = random.randint(a, b)
    while random_var in list_a: # もし重複したら、もう一度乱数を生成します。
        random_var = random.randint(a, b)
    list_a.append(random_var) # 乱数の範囲は1～9
    list_a_pick_flag.append(0)
# print(list_a)
# print(list_a_pick_flag)

# 選択したインターフェース
for i in range(len(list_a_pick_flag)):
    if list_a_pick_flag[i] == 0:
        print("*", end = " ")
    else:
        print(list_a[i], end = " ")

# game       
player_points = 0
computer_points = 0

while list_a_pick_flag.count(0) > 1: 
    player_pick = int(input("choose one:"))
    while list_a_pick_flag[player_pick] !=0 : # もし重複したら、もう一度選択してください
        player_pick = int(input("Choose again:"))
    player_pick_n = list_a[player_pick] # 選択した番号
    list_a_pick_flag[player_pick] = 1 # 選択した場所にマークを付ける
    
    computer_pick = random.randrange(len(list_a_pick_flag))
    while list_a_pick_flag[computer_pick] !=0 :  # もし重複したら、もう一度乱数を生成します。
        computer_pick = random.randrange(len(list_a_pick_flag))
    computer_pick_n = list_a[computer_pick]
    list_a_pick_flag[computer_pick] = 1  # 選択した場所にマークを付ける  
    
    # 選択したインターフェースを更新する
    for i in range(len(list_a_pick_flag)):
        if list_a_pick_flag[i] == 0:
            print("*", end = " ")
        else:
            print(list_a[i], end = " ")  
    print("")
    # 選択した値を表示します
    print("player_pick_n: {}".format(player_pick_n))    
    print("computer_pick_n: {}".format(computer_pick_n)) 
    
    # 誰がポイントを獲得するかを比較する
    if player_pick_n >= computer_pick_n:
        player_points+=player_pick_n + computer_pick_n
        print("The player wins {} points.".format(player_pick_n + computer_pick_n))
    else:
        computer_points+=player_pick_n + computer_pick_n
        print("The computer wins {} points.".format(player_pick_n + computer_pick_n))

print("------------------------end------------------------------------")
print("The computer wins {} points.".format(computer_points))
print("The player wins {} points.".format(player_points))
if player_points >= computer_points:
    print("The player wins the game.")
else:
    print("The computer wins the game.")