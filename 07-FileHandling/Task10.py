with open('student.txt', 'w', encoding='UTF-8') as f:
    f.write('Małgorzata Leśniak\n')
    f.write('Uniwersytet Ekonomiczny w Krakowie\n')
    f.write('221375\n')

#ALBO (lepiej to na dole)

file = open('student.txt', 'w')
file.write('Małgorzata Leśniak\n')
file.write('Uniwersytet Ekonomiczny w Krakowie\n')
file.write('221375\n')

file.close()