print ("Welcome to the tip Calculator")
total_bill = input("what was the total bill? $")
percentage = input ("what percentage would you like to give? 10, 12, or 15? ")
new_percentage = int(percentage)/100 
Number_of_people =input("how many people to split the bill? ")
new_bill = (new_percentage * (float(total_bill))) + (float(total_bill))
tip = new_bill / (int(Number_of_people))
new_tip = (round(tip, 2))
print (f"Each person should pay: ${new_tip}")
##wonderful

