array = [-15, 8, -31, 47, -2, 19]

max_val = array[0]
min_val = array[0]

for i in array:
    if i>=max_val:
        max_val=i
    elif i<=min_val:
        min_val=i

print(f"Maximum value is {max_val} and minimum value is {min_val}.")
