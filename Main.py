import random
from os import system
import time

def clearConsole():
    """städar bort saker i terminal"""
    system("cls || clear")

class Player: #Player klassen
    def __init__(self, health, strength, level, player_name):
        self.health = health 
        self.strength = strength
        self.level = level 
        self.name = player_name
        self.inventory = []

    def check_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(f"{item.weapon_type}, Styrkaökning: +{item.damage}")
        else:
            print("Ditt inventory är tomt.")

    def removefrominventory(self, itemposition):
        self.inventory.remove[itemposition]
        print(f"{self.inventory[itemposition]} har blivit borttaget")


class Item:
    def __init__(self, weapon_type, strength):
        self.weapon_type = weapon_type
        self.damage = strength

class Monster:
    def __init__(self, playerLevel):
        strength = random.randint((playerLevel-1)*2, playerLevel*2+2)
        if playerLevel >= 10:
            print(f"Grattis!!! Du vann {player.name}")
            strength = random.randint(69, 420)
        self.strength = strength
        monster_names = ["Taurus", "Bulten", "Muttern", "Krampus", "Stinger"]
        self.name = random.choice(monster_names)

# Här skapas vapen och exempel på spelare
def generateitem():
    random_strength_bonus = random.randint(0, 10)
    weapons = [Item("Pilbåge", random_strength_bonus), Item("Svärd", random_strength_bonus), 
            Item("Lans", random_strength_bonus), Item("Pinne", random_strength_bonus)]
    weapons = random.choice(weapons)
    return weapons

def get_name(): # funktion till playerns nametag
    player_name = input("Namn: ")
    return player_name 

# Här läggs funktioner för att interagera med spelet

def check_health(player, damagedelt):
    player.health -= damagedelt
    print(f"Du har {player.health}hp kvar")
    if player.health <= 0:
        print("Du förlora! get good!")
        if_continue = input("tryck på W för att fortsätta:")
        if if_continue == "W" or "w":
            clearConsole()
            start()
        else:
            exit()
    else:
        pass
            
def reveal_monster(player):
    monster = Monster(player.level)
    print(f"Det var ett monster bakom dörren! Det var {monster.name}")
    fight(player, monster)

def reveal_chest(player):
    treasure = generateitem()
    print(f"Du hittade en kista! I den låg en {treasure.weapon_type}")
    if len(player.inventory) == 5:
        while True:
            print("Ditt inventory är fullt! Vill du ta bort ett item och byta ut det? ja/nej")
            var = input()
            if var == "nej":
                break
            elif var == "ja":
                player.removefrominventory(0)
                break
            else:
                pass
    else:                   
        player.inventory.append(treasure)


def reveal_trap(player):
    print("Det var en fälla bakom dörren, din karaktär förlorade ett liv")
    check_health(player, 1)    

def fight(player, monster):
    fighting = input("Tryck A om du vill attackera, eller S för att förlora 2 hp och gå vidare! : ")
    if fighting == "A" or "a":
        print(f"Du möter {monster.name}")
        damage(monster, player)
    elif fighting == "S" or "s":
        player.health -= 2

def damage(monster, player):
    if monster.strength > player.strength:
        damagedelt = 1
        check_health(player, damagedelt)
        print("Du förlora mot monstret")
    else:
        player.level += 1
        player.strength += 1
        print("Du vann och gick upp i level, Grattis!")
        time.sleep(2)


def start_labyrint():
    #omskrivningsdags!!!!
    player_name = get_name()
    player = Player(10, 1, 1, player_name)
    print(f"Ditt äventyr har börjat {player_name}")
    time.sleep(2)
    spel()

    """while True:
        if answer.lower() == "ja":
            player_name = get_name() # skickar dig till name_tag funktionen om du skriver yes
            advetnture_start = print(f"Ditt äventyr har börjat {player_name}")
            return advetnture_start
        elif answer.lower() == "nej":   # Om no är input frågar programet om du vill avsluta spelet
            end = input("Vill du avsluta spelet? ")
            if end == "ja": # programet ska avslutas, hur man nu gör det
                exit()
            elif end.lower() == "nej": # om man skriver no ska man tillbaka till första if statement
                start_labyrint(input("Vill du fortsätta ditt äventyr? "))
                pass
            else:
                wrong_written(answer)
                start_labyrint(answer)
                break
        else:
            wrong_written(answer) # om man inte skriver yes eller no får de reda på det, vill att det ska skickas till första if
            start_labyrint(answer)
            break"""

def wrong_written(answer):
    if not answer == "ja" or "nej":
        print("Det är en ja eller nej fråga!")
    else:
        pass

advetnture_start = ""

def get_name(): # funktion till playerns nametag
    player_name = input("Namn: ")
    return player_name 



def chose_door(player):
    print(f"""
Framför dig står tre dörrar. Bakom dörrarna kan det finnas en fälla, ett monster eller en kista.
Du {player.name} har ett val.
Välj smart!
    """)
    input("Vad väljer du: dörr 1, 2 eller 3? ")
    val = random.randint(1,3)
    if val == 1:
        reveal_monster(player)
    elif val == 2:
        reveal_chest(player)
    elif val == 3:
        reveal_trap(player)

def start():
    answer = input("Vill du börja ditt ävnentyr? ")
    if answer == "ja":
        start_labyrint()
    elif answer == "nej":
        print("Okej :(")
        exit()
    else:
        print("Det är en ja/nej fråga!!!!!!")
        start()

def spel():
    while True:
        
        command = input("Tryck 'i' och Enter för att kolla ditt inventory, eller annan tangent för att fortsätta: ")
        if command.lower() == 'i':
            player.check_inventory()
        chose_door(player)

start()