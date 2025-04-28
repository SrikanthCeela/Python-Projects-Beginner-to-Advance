# Banker Roulette
# Who will pay the bill
import random

friends = input("Enter names of your friends separated by space: ").split()

# print(len(friends))

roll = random.randint(0,len(friends) - 1)

# print(roll)

print(f'The person who pays the bill is "{friends[roll]}"')