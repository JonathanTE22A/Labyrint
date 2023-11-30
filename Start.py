import monster
import sys

def start_labyrint(resultat):
    while True:
        if resultat.lower() == "ja":
            player_name = get_name() # skickar dig till name_tag funktionen om du skriver yes
            adventure_start(player_name)
            break
        elif resultat.lower() == "nej":   # Om no är input frågar programet om du vill avsluta spelet
            end = input("Vill du avsluta spelet? ")
            if end == "yes": # programet ska avslutas, hur man nu gör det
                exit()
            elif end.lower() == "nej": # om man skriver no ska man tillbaka till första if statement
                start_labyrint(input("Vill du fortsätta ditt äventyr? "))
                break
            else:
                wrong_written()
        else:
            wrong_written() # om man inte skriver yes eller no får de reda på det, vill att det ska skickas till första if
            break

def adventure_start(player_name): #får veta att spelat ska börja
    print(f"Ditt äventyr har börjat {player_name}") 

def get_name(): # funktion till playerns nametag
    player_name = input("Name: ")
    return player_name 

def wrong_written():
    if not input == "ja" or "nej":
        print("Det är en ja eller nej fråga!")


resultat = start_labyrint(input("Vill du börja ditt ävnentyr? "))
# player_name = name_tag(input("Name : "))

