
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi <= 18:
    print(f"Your Bmi is {bmi}, you are underweight.")
elif bmi <= 22:
    print (f"Your Bmi is {bmi}, you have a normal weight.")
elif bmi <= 28:
    print (f"Your Bmi is {bmi}, you are slightly overweight.")
elif bmi <= 33:
    print (f"Your Bmi is {bmi}, you are obese.")
else:
    print (f"Your Bmi is {bmi}, you are clinically obese.")



