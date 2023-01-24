names = ['Anna', 'Oskars', 'Jenifer', 'Anna', 'Miks']
ages = [17, 18, 18, 15, 20]

numbers = range(len(names))

for number in numbers:
    print(f'{names[number]} is {ages[number]} years old')