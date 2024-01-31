import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword generator!")
letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))
numbers_count = int(input("How many numbers would you like in your password?\n"))
password_length = letter_count + symbol_count + numbers_count

# Generate password
password = []

while len(password) < password_length:
    random_symbol = random.choice([1, 2, 3])

    if random_symbol == 1 and letter_count > 0:
        password.append(random.choice(letters))
        letter_count -= 1
    elif random_symbol == 2 and symbol_count > 0:
        password.append(random.choice(symbols))
        symbol_count -= 1
    elif random_symbol == 3 and numbers_count > 0:
        password.append(random.choice(numbers))
        numbers_count -= 1

print("Generated Password:", ''.join(password))
