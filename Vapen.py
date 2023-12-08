import random

class Item:
    def __init__(self,weapon_type, damage, critchanse):
        self.weapon_type = weapon_type
        self.damage = damage
        self.critchanse = critchanse

    def presentweapon(self):
        print("Du hittade " + self.weapon_type + " som gör "  + self.damage+ " skada och har en critchanse på " + self.critchanse+"%")
exp = ""


def Level_system(): 
    if monster_hp() < player_hp():
        level_up()
    

def level_up():
    if exp == 1:
        list = [Weapon1,Weapon2,Weapon3,Weapon4]
        print(random(list))



Weapon1 = Item("Pilbåge", 15, 32)
Weapon2 = Item("Svärd", 20, 10)
Weapon3 = Item("Lans", 25, 5)
Weapon4 = Item("Pinne", 8, 50)
class Inventroy:
    def __init__(self):
        self.items : list[Item] = []
    
    def print(self):
        for item in self.items:
            print(item)