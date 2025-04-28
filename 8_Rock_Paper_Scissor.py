import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

user_choice = int(input('''
                        What do you choose?
                        Type 0 for Rock,
                        Type 1 for Paper,
                        Type 2 for Scissors
                        '''))

if user_choice >= 3 or user_choice < 0:
    print("You Typed a wrong number!")
else:
    print(f"You chose\n{game_image[user_choice]}\n")

    computer_choice = random.randint(0,2)
    print(f"Computer chose\n{game_image[computer_choice]}")


    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("That's a draw")