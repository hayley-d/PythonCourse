print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Do you want to go left ro right?")
if direction == "left":
    print("You are eaten my a giant sloth!\nGame Over :(")
else:
    print("You approach a lake, you can either swim across or wait")
    swim = input("Do you swim or wait?")
    if swim == "swim":
        print("While you swim accross, you are eaten by a hungry sea star!\nGame Over :(")
    else:
        print("After about 5 minuets of waiting, a gint sloth arrives, you hop on its back and it helps you accross the lake.")
        print("You keep walking an eventually approach three doors, a blue door, green door and pink door")
        door = input("What colour door do you enter?")
        if door == "blue":
            print("You enterr the blue door only to find that you are back where you started.\nGame Over :(")
        if door == "green":
            print("You enterr the green door and find the mad hatter is having a tea party and you have an invitation.\nGame Over :(")
        if door == "pink":
            print("You enter the pink door and find you are in the land of the slots.\n Well done you won!!\nGame Over :(")
