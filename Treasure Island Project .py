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
print("Welcome to the mysterious and wonderful Treasure Island.")
print("Your sole mission is to dig aorund and find the treasure. Beware of the choices you make they decide your wealth !!")
choice = input ("You have come to a Junction with two paths in front of you, which one will you choose left or right ?")
if choice == "right":
    print ("You have chosen wronglyy !!! and you fall in a hole and die. Game over !!!")
elif choice == "left":
    print = choice =input ("You chose the right path as you move forward and you come to a river with an island in the middle do you 'swim' or 'wait' for a boat?")
else :  
  print ("game over")
  if choice == "swim":
    print ("Halfway through the river you encounter a hoard of piranhas who tear you limb from limb. Game Over !!!")
  elif choice == "wait":
    print = choice2 = input ("Your Patience has paid off, A boat comes that takes you to the Island where you encouter three doors with the color 'red','yellow','blue', choose one")
  else:
    print ("Game Over !!")
  if  choice2 == "red":
    print ("You enter into a flaming lake of fire which burns you to death. Game   Over !!!")
  elif choice2 == "blue":
    print ("You dive into a wide ocean where whales gobble you up. Game Over ")
  elif choice2 == "Yellow":
    print ("you won!!")
  else:
    print ("Game Over !!")
