# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:16:27 2021

@author: Fenrir

Description :
    
override

Human
  name, age, career
  information, grow_old
  
Vampire
  + hunger_percent
  + suck_blood
  * information
Werewolf
  + is_wolf
  + change_state  
  * information
"""
class Human:
    """Human class """
    # Constructor
    def __init__(self, _name, _age, _career):
        # member
        self.name = _name
        self.age = _age
        self.career = _career
        
    # method
    def information(self):
        text = "Name: {}\nAge: {}\nCareer: {}\n"
        return text.format(self.name, self.age, self.career)
    
    def grow_old(self, after):
        self.age += after

class Vampire(Human):
    """Vampire class inheritance """
    # Constructor
    def __init__(self, _name, _age, _career, _hunger_percent):
        # スーパークラスのコンストラクタを呼び出す
        super().__init__(_name, _age, _career)
        self.hunger_percent = _hunger_percent
        
    # メソッドを追加
    def suck_blood(self, blood):
        self.hunger_percent += blood
    # メソッドをオーバーライド
    def information(self):
        text = "Name: {}   Age: {}\nCareer: {}\nHunger percent: {}%\n"
        return text.format(self.name, self.age, self.career, self.hunger_percent)
    
class Werewolf(Human):
    """Werewolf class inheritance """
    # Constructor
    def __init__(self, _name, _age, _career, _is_wolf):
        # スーパークラスのコンストラクタを呼び出す
        super().__init__(_name, _age, _career)
        self.is_wolf = _is_wolf
        
    # メソッドを追加
    def change_state(self):
        self.is_wolf = not self.is_wolf
    # メソッドをオーバーライド
    def information(self):
        text = "Name: {}   Age: {}\nCareer: {}\n"
        if self.is_wolf:
            text += "State : Wolf\n"
        else:
            text += "State : Human\n"
        return text.format(self.name, self.age, self.career)

human_a = Human("Rize", 16, "Soldier")
print(human_a.information())
    
edward = Vampire("Edward Anthony Masen", 120, "Vampire", 60)
print(edward.information())

edward.suck_blood(10)
edward.grow_old(100)
print(edward.information())


jacob = Werewolf("Jacob Black", 31, "Werewolf", False)
print(jacob.information())

jacob.change_state()
jacob.grow_old(5)
print(jacob.information())