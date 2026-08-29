import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to pass generator")
nr_letters = int(input("HOw many letters would you like in your password\n"))
nr_symbols = int(input("HOw many symbols would you like in your password\n"))
nr_numbers = int(input("HOw many numbers would you like in your password\n"))

password=''
for i in range(nr_letters):
    password+=random.choice(letters)

for i in range(nr_symbols):
    password+=random.choice(symbols)

for i in range(nr_numbers):
    password+=random.choice(numbers)

letters= list(password)
print(letters)
random.shuffle(letters)
print(letters)