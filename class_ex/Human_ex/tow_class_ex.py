# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:07:41 2021

@author: Fenrir

Description :
Vampire
  name, age, career, hunger_percent
  information, grow_old, suck_blood
Werewolf
  name, age, career, is_wolf
  information, grow_old, change_state
"""
class Vampire:
    """Vampire class """
    # Constructor
    def __init__(self, _name, _age, _career, _hunger_percent):
        
        # member
        self.name = _name
        self.age = _age
        self.career = _career
        self.hunger_percent = _hunger_percent
        
    # method
    def information(self):
        text = "Name: {}   Age: {}\nCareer: {}\nHunger percent: {}%\n"
        return text.format(self.name, self.age, self.career, self.hunger_percent)
    
    def grow_old(self, after):
        self.age += after

    def suck_blood(self, blood):
        self.hunger_percent += blood
        
class Werewolf:
    """Werewolf class """
    # Constructor
    def __init__(self, _name, _age, _career, _is_wolf):
        
        # member
        self.name = _name
        self.age = _age
        self.career = _career
        self.is_wolf = _is_wolf
        
    # method
    def information(self):
        text = "Name: {}   Age: {}\nCareer: {}\n"
        if self.is_wolf:
            text += "State : Wolf\n"
        else:
            text += "State : Human\n"
        return text.format(self.name, self.age, self.career)
    
    def grow_old(self, after):
        self.age += after

    def change_state(self):
        self.is_wolf = not self.is_wolf
        
        
# main
# Instance object

edward = Vampire("Edward Anthony Masen", 120, "Vampire", 60)
print(edward.information())

jacob = Werewolf("Jacob Black", 31, "Werewolf", False)
print(jacob.information())

edward.suck_blood(10)
edward.grow_old(100)
print(edward.information())

jacob.change_state()
jacob.grow_old(5)
print(jacob.information())
