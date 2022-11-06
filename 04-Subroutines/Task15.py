import mymath

user_number=mymath.read_number()
the_number=mymath.generate_number()

while user_number != the_number:
    user_number = mymath.read_number()

print("You win!")