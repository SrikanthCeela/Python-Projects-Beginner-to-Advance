print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill? $"))

tip_percent = float(input("how much percent of the tip would you like to give?e.g., 10, 12 or 15?: "))

tip = (tip_percent/100) * bill

total_bill = bill + tip

person = int(input("How many people to split the bill? "))

bill_per_person = total_bill / person

print(f"Each person should pay: ${bill_per_person:.2f}")


