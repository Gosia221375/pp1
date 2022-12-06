array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

curr_max=0
curr_name=""

for i in range(len(array)):
    if len(array[i])>=curr_max:
        curr_max=len(array[i])
        curr_name=array[i]

print(f"Names: {array}")
print(f"Longest name: {curr_name}")