import random

def read_number():
    x = int(input("Enter a number: "))
    return x

def generate_number():
    generated = random.randint(1,9)
    return generated