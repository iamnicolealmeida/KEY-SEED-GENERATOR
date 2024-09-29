import random, os

numbers = []

for i in range(10):
    number = random.randint(1, 999)
    numbers.append(number)

os.system('cls' if os.name == 'nt' else 'clear')

output = ''.join(map(str, numbers))

print(output)
