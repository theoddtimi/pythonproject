
##DATA TYPES
# num_char = len(input("what is your name?"))
# #convert the integer first
# new_num_char = str(num_char)
# print("your name has " + new_num_char + " characters")
# you can use a type check option to know what the data you are working with is, 
# print(type(num_char)) will show you this <class 'int'>
# a = str(567)
# print (type(a))
#WHEN IT COMES TO PATA TYPES OPERATIONS, PEMDASLR  IS FOLLOWED
# print (round(11//3))
# score = 5+1
# score += 1
# print (score)

# F-string
# score = 10
# height = 1.9
# winning = True 
# print(f"your score is {score} your height is {height} you are winning, true or false?: {winning}")
# print (round(10/3, 2))


### Day 3 notes else if operations

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# put = sign to include 120 in the if category
print ("Welcome to the Rollercoaster")
height = int(input("What is your height "))
if height > 120:
  bill=0
  print ("You can ride the roller coaster")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print ("Child Tickets are $5.")
  elif age <= 18 :
    bill = 7
    print ("Youth Tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  wants_photo = input ("Do you want a Photo Taken? Y or N ")
  if wants_photo =="Y":
    #Add $3 to their Bill 
    bill += 3
  print (f"Your final bill is ${bill}")

else:
  print ("Sorry, you have to grow taller before you can ride")

#   operations include
# > means greater than
# < means lesser than
# >= means greater than or equal to
# <= means lesser than or equal to
# == means equal to
# != means not  to
#  note that 2 equal signs should be used during else if variables


#Logical Operators
# A "and" B
# C "or" D
# "not"
#
no of t in 