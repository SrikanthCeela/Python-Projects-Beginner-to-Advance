# BMI Calculator with Interpretations
"""
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"
"""
weight = float(input("What is your weight in kg: "))
height = float(input("What is your height in m: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are Underweight!")
elif bmi < 25:
    print("You are normal weight!")
else:
    print("You are Overweight!!!")