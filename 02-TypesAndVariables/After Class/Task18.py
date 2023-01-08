a = int(input("Enter the lenght of the side A: "))
b = int(input("Enter the lenght of the side B: "))
c = int(input("Enter the lenght of the side C: "))

s = (a + b + c)/2

area = (s*(s-a)*(s-b)*(s-c))**(1/2)

print(area)