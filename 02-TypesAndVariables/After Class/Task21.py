import random

dice = random.randint(1,6)
guess = int(input("Enter a number from 1 to 6: "))

print(dice == guess)