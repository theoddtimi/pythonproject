# Instructions
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

age = input("What is your current age? ")
y = (90 - int(age)) * 52
x = (90 - int(age)) * 365 
z = (90 - int(age)) * 12
print (f"You have {x} days, {y} weeks, and {z} months left ")