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

# Write your code below this line 👇

print("You are at a crossroad. You see an old, mysterious map in your hands, guiding your way through the dense jungle.")

choice1 = input('Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    print("You decided to follow the narrow path into the dark forest. You hear strange whispers around you.")
    choice2 = input('You\'ve come to a lake with dense fog. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        print("The fog clears as a boatman emerges from the mist, guiding you safely to the island.")
        choice3 = input("You arrive at the island. There is a grand mansion with 3 doors: red, yellow, and blue. Each door is adorned with ancient symbols. Which door do you choose? \n").lower()
        if choice3 == "red":
            print("As you open the red door, a gust of hot wind knocks you back. You've entered a chamber of lava streams. Game Over.")
        elif choice3 == "yellow":
            print("You open the yellow door and step into a room filled with shining gold and jewels. Congratulations! You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You open the blue door and find yourself facing growling wolves. They pounce as you enter. Game Over.")
        else:
            print("You chose a door that doesn't exist. You stumble into darkness. Game Over.")
    else:
        print("You decide to swim across the lake. Halfway through, you realize the lake is infested with crocodiles. Game Over.")
else:
    print("You head towards the right path and find an ancient temple entrance. Excitedly, you step inside.")
    print("Inside the temple, you encounter a series of puzzles and traps. You navigate carefully but one wrong step triggers a trap door. Game Over.")

print("\nThank you for playing!")
