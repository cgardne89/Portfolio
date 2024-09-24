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

def get_user_input(question, modes):
    while True:
        user_input = input(question).lower()
        if user_input in modes:
            modes[user_input]()
            break
        else:
            print("Error: Please select a valid mode:\n" + ", ".join(modes) + " ")

def get_password():
    password.append("Password: ")
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
        return password

def get_website():
    password.append(" Website: ")
    user_input = input("Website for password: ")
    password.append(user_input)
    return password

def store_info():
    while True:
        user_input = input("Would you like to store your password? ").lower()
        if user_input == "yes":
            print("storing....")
            with open("passwords.txt", "a") as file:
                file.write("".join(password))
                print("password saved")
        break

def erase_info():
    while True:
        user_input = input("Would you like to remove all passwords? ").lower()
        if user_input == "yes":
            print("removing....")
            with open("passwords.txt", "w") as file:
                file.write("")
                print("passwords removed")
        break

def get_cryptography_type():
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
while True:
    modes = {"create password": get_password, "cryptography": get_cryptography_type, 
             "enter website": get_website, "save file": store_info,
             "delete file": erase_info, "quit": quit}

    question = "Mode: "
    get_user_input(question, modes)

