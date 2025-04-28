'''
Create a coin flip program using what you have learnt about randomisation in python.
It should randomly print "Heads" or "Tails" everytime it is run
'''
import random

toss = random.randint(0,1)
print(toss)

if toss == 0:
    print("Heads")
else:
    print("Tails")
