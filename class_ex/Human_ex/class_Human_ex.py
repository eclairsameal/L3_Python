# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 11:34:47 2021

@author: Fenrir

Description :

Human
  name, age, career
  information, grow_old
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
        text = "Name: {}\nAge: {}\nCareer: {}"
        return text.format(self.name, self.age, self.career)
    
    def grow_old(self, after):
        self.age += after
    
    
human_a = Human("Rize", 16, "Soldier")
# human_b = Human("Kokoa", 15, "Bakers")
human_c = Human("Chino", 13, "Coffee maker")
# student
"""
print("Name: {}".format(human_a.name))
print("Age: {}".format(human_a.age))
print("Career: {}".format( human_a.career))

human_b = Human("Kokoa", 15, "Student")
print("Career: {}".format( human_b.career))
human_b.career = "Bakers"
print("Career: {}".format( human_b.career))
"""
human_c = Human("Chino", 13, "Coffee maker")
print(human_c.information())
human_c.grow_old(3)
print(human_c.information())

