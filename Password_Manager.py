# Password Manager
import string
import random

# lists
alphebet = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)
spaces = list(string.whitespace)
password = []
encrypted_password_storage = {}

# modules

def get_user_input():
    while True:
        user_input = input("What would you like to do today? ").lower()
        if user_input == "cryptography":
            get_crytography_type()
            break
        if user_input == "create password":
            get_password()
            break
        else:
            print("Error: create password or crytography")

def get_password():
    while True:
        randomize = random.randrange(14, 16)
        for i in range(randomize):
            if i % 2 == 0:
                if random.randrange(0, 2) == 1:
                    letter = alphebet[random.randrange(0, 26)]
                    password.append(letter.upper())
                else:
                    letter = alphebet[random.randrange(0, 26)]
                    password.append(letter)
            if i % 3 == 0:
                number = numbers[random.randrange(0, 10)]
                password.append(number)
            if i % 5 == 0:
                symbol = symbols[random.randrange(0, 25)]
                password.append(symbol)
        print("".join(password))
        store_password()
        return password

def store_password():
    while True:
        user_input = input("Would you like to store your password? ").lower()
        if user_input == "yes":
            print("storing....")
            with open("passwords.txt", "a") as file:
                file.write("".join(password) + "\n")
                print("password saved")
        break

def get_crytography_type():
    while True:
        crytography = input("Cryptography: ").lower()
        if crytography == "encrypt" or crytography == "decrypt":
            get_shift_amount()
            break
        else:
            print("Error: Do you want to Encrypt or Decrypt?")
            continue

def get_shift_amount():
    while True:
        shift = input("Shift: ")
        if not shift.isnumeric():
            print("Must be a positive number")
            continue
        shift = int(shift)
        get_phrase()
        return shift

def get_phrase():
    while True:
        phrase = input("Phrase: ")
        for char in phrase:
            if char in spaces:
                print("Must have no spaces")
                break
        else:
            return phrase
# user input
get_user_input()
