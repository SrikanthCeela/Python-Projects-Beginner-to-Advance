"""
Write a Pizza Delivery Program
COngratualtions, You've got a job at python pizza!Your first job is to build an automatic pizza order program

Based on user's order, work out their final bill
Use the input() function to get a user's preferences 
and then add up the total of their order 
and tell them how much they have to pay

small pizza (S): $15
Medium Pizza (M): $20
Large Pizza (L): $25

Add pepporoni for small pizza(Y or N): +$2
Add pepporoni for Medium or large pizza(Y or N): +$3

Add extra cheese for any sze pizza( Y or N): +$1


"""

print("Welcome to Python pizza deliveries!")
size = input("What size of pizza do you want? S, M, L: ").upper()
pepporoni = input("Do you want pepporoni to your pizza? Y or N: ").upper()
cheese = input("Do you want an extra cheese? Y or N: ").upper()

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You types a wrong input")


if pepporoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1

print(f"You final bill is ${bill}")