def f(human_age):
    value =0
    for x in range(1,int(human_age)+1):
        if x<3:
            value += 10
        else:
            value+=4
    return value



age = input("age: ")

print(f(age))