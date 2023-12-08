import random


class Player:
    def __init__(self, health, strenght, level, player_name):
        self.health = health 
        self.strenght = strenght
        self.level = level 
        self.name = player_name
        self.inventroy = []

class Inventory():
    def __init__(self):
        self.items: list[Item] = []
    
inventory = Inventory()

class Item:
    def __init__(self,weapon_type, strenght):
        self.weapon_type = weapon_type
        self.damage = strenght


random_strenght_bonus = 2
Weapon1 = Item("Pilbåge", random_strenght_bonus)
Weapon2 = Item("Svärd", random_strenght_bonus)
Weapon3 = Item("Lans", random_strenght_bonus)
Weapon4 = Item("Pinne", random_strenght_bonus)


class Monster:
    def init(self, playerLevel):
        # Sets strength according to player level
        strength = 0
        strength = random.randint((playerLevel-1)*2, playerLevel*2+2)

        if playerLevel >= 10:
            strength = random.randint(69,420)

        self.strength = strength

        # Sets random name
        monster_names = ["Taurus", "Bulten", "Muttern", "Krampus", "Stinger"]
        chosen_name = random.choice(monster_names)
        self.name = chosen_name

monster = Monster()

def reveal_monster(chosen_name):
    print(f"Det var ett monster bakom dörren! Det var {chosen_name}")
    fight()

def reveal_paket(inventory):
    tresure = Item.random.randint(1,4)
    print(f"Du hittade en kista! I den låg en {tresure}")
    Item.strenght =+ 1
    inventory.append(tresure)

def reveal_trap(p: Player):
    print("Det var en fälla bakom dörren, din karaktär förlorade ett liv")
    p.health = -1
    chose_door()
    return p.health

def fight():
    global player
    monster = Monster(player.level)
    fighting = input("Tryck A om du vill attacker, eller S för att förlora 2 hp och gå vidare! : ")

    if fighting == "A":
        print(f"Du möter {monster.name}")
        damage(monster, player)
    elif fighting == "S":
        player.health =- 2  

def damage(m: Monster, p: Player):
    if  m.strength > p.strenght:
        p.health =- 1

    else:
        p.level =+ 1


#inventory.items.append()

#inventory.print()

player = Player(10, 3, 1 , "Kaoz")


def start_labyrint(answer):
    while True:
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
                break
        else:
            wrong_written(answer) # om man inte skriver yes eller no får de reda på det, vill att det ska skickas till första if
            break

def wrong_written(answer):
    if not input == "ja" or "nej":
        print("Det är en ja eller nej fråga!")

advetnture_start = ""

def get_name(): # funktion till playerns nametag
    player_name = input("Namn: ")
    return player_name 

answer = start_labyrint(input("Vill du börja ditt ävnentyr? "))

def chose_door(player_name):

    print(f"""
          

Framför dig står det tre dörrar. Bakom dörrarna kan det finnas en fälla, ett monster eller en kista.
Du {player_name} har ett val.
välj smart!
          """) # spelaren väljer en dörr
    val = int(input("""
Vad väljer du
dörr 1,2 eller 3
"""))
    val = random.randint(0,2)
    if val == 0:
        reveal_monster(Monster.)
    elif val == 1:
        reveal_paket()
    elif val == 2:
        reveal_trap()

chose_door(player.name)
