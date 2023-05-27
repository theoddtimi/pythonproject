height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = (int(weight/ height **2))
if bmi < float(18.5):
    print ("Your BMI is {bmi}, you are underweight ")
else:
    print ("you are good to go") 