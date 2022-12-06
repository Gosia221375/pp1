array = [
    {"country": "Poland", "population": 38000000},
    {"country": "Italy", "population": 59000000},
    {"country": "Germany", "population": 83000000},
    {"country": "Russia", "population": 146000000},
    {"country": "Ukraine", "population": 41000000},
]

i = 0
while i < len(array):
    for key, value in array[i].items():
        print(key, " - ", value, end = " ")
    i = i + 1
    print()



# ctrl + c żeby zatrzymać nieskończony program