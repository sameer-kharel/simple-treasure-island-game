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

first_case = input("Where do you wanna go n the life? Enter 'L' for left or 'R' for right:\n ")

if first_case.lower() == "l":
    second_case = input("Do you want to swim or walk? Enter 'S' for swim or 'W' for walk:\n ")

    if second_case.lower() == "w":
        third_case = input("There are three ways to reach the destination. If you want to go by the Parkway Choose 'A', Avenue choose 'B', or 'C' for the Highway:\n ")

        if third_case.lower() == "a":
            print("You are burned by the fire. Game Over.")
        elif third_case.lower() == "b":
            print("You are eaten by the beasts. Game Over.")
        elif third_case.lower() == "c":
            print("Congratulations! You have reached your destination. Enjoy!")
        else:
            print("Game Over")
    elif second_case.lower() == "s":
        print("You are attacked by trout. Game Over.")
    else:
        print("Game Over.")

elif first_case.lower() == "r":
    print("You just fell into a hole. Game Over.")

else:
    print("Game Over.")


  
