# importing stuff we need
import random  # this is for random numbers and choices
import base64  # to encode things
import os      # for interacting with the system
import string  # has letters and stuff

# importing cryptography modules
from cryptography.fernet import Fernet  # for encryption and decryption
from cryptography.hazmat.primitives import hashes  # for hashing
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # key derivation

# lists of characters to use
alphabet = list(string.ascii_letters)  # all letters
numbers = list(string.digits)          # numbers from 0 to 9
symbols = list(string.punctuation)     # symbols like !,@,#,$
password = []  # empty list to store password parts

# function to make a key using password and salt
def generate_key(password_provided, salt):
    password_bytes = password_provided.encode()  # turn password into bytes
    kdf_instance = PBKDF2HMAC(  # key derivation function
        algorithm=hashes.SHA256(),  # use SHA256
        length=32,                  # key length is 32 bytes
        salt=salt,                  # the salt
        iterations=100000,          # do it 100,000 times
    )
    key = base64.urlsafe_b64encode(kdf_instance.derive(password_bytes))  # derive key
    return key  # give back the key

# function to get user input and run the right mode
def get_user_input(question, modes):
    while True:
        user_input = input(question.lower())  # ask the user
        if user_input in modes:
            modes[user_input]()  # run the function they chose
            break
        else:
            print("Error: Please select a valid mode:\n" + ", ".join(modes) + " ")  # tell them it's wrong

# function to make a random password
def get_password():
    placeholder_password = ""  # start with empty password
    randomize = random.randrange(14, 16)  # pick a length between 14 and 15
    for i in range(randomize):
        if i % 2 == 0:
            letter = random.choice(alphabet)  # pick a random letter
            # sometimes make it uppercase
            placeholder_password += letter.upper() if random.choice([True, False]) else letter
        if i % 3 == 0:
            number = random.choice(numbers)  # pick a random number
            placeholder_password += number
        if i % 5 == 0:
            symbol = random.choice(symbols)  # pick a random symbol
            placeholder_password += symbol
    return placeholder_password  # give back the password

# function to encrypt the password
def encrypt_password():
    password.append("Password: ")  # add "Password: " to list
    shift = get_shift_amount()     # get the shift amount
    phrase = get_password()        # generate the password
    print(f"Generated password before encryption: {phrase}")  # show the password
    for char in phrase:
        if char in alphabet:
            index = alphabet.index(char.lower())  # find the index of the letter
            shifted_char = alphabet[(index + shift) % 26]  # shift it
            # keep the case the same
            password.append(shifted_char.upper() if char.isupper() else shifted_char)
        elif char in numbers:
            index = numbers.index(char)  # find the index of the number
            password.append(numbers[(index + shift) % 10])  # shift it
        elif char in symbols:
            index = symbols.index(char)  # find the index of the symbol
            password.append(symbols[(index + shift) % len(symbols)])  # shift it
    get_website()  # ask for website

# function to decrypt the password
def decrypt_password():
    decrypt_password = []  # list to store decrypted chars
    shift = get_shift_amount()  # get the shift amount
    phrase = input("Enter the encrypted phrase: ")  # ask for the encrypted password
    for char in phrase:
        if char in alphabet:
            index = alphabet.index(char.lower())  # find index
            shifted_char = alphabet[(index - shift) % 26]  # shift back
            # keep case same
            decrypt_password.append(shifted_char.upper() if char.isupper() else shifted_char)
        elif char in numbers:
            index = numbers.index(char)
            decrypt_password.append(numbers[(index - shift) % 10])  # shift back
        elif char in symbols:
            index = symbols.index(char)
            decrypt_password.append(symbols[(index - shift) % len(symbols)])  # shift back
        else:
            decrypt_password.append(char)  # just add it if not found
    print("Decrypted password: " + "".join(decrypt_password))  # show the decrypted password

# function to get the website
def get_website():
    password.append(" Website: ")  # add " Website: " to list
    user_input = input("Website for password: ")  # ask for website
    password.append(user_input)  # add it to list
    store_info()  # store the info

# function to store the info securely
def store_info():
    if os.path.exists("passwords.txt"):
        password_provided = input("Enter your password to unlock the file: ")  # ask for file password
        try:
            with open("passwords.txt", "rb") as file:
                salt = file.read(16)  # read the salt
                encrypted = file.read()  # read the encrypted data
            key = generate_key(password_provided, salt)  # generate key
            fernet = Fernet(key)  # make Fernet object
            decrypted = fernet.decrypt(encrypted)  # decrypt data
            data = decrypted.decode() + "\n" + "".join(password)  # add new password
            encrypted = fernet.encrypt(data.encode())  # encrypt data
            with open("passwords.txt", "wb") as file:
                file.write(salt + encrypted)  # write back to file
            print("Password saved and encrypted.")
        except Exception as e:
            print("Incorrect password or error decrypting the file.")  # error message
    else:
        password_provided = input("Set a password to protect your file: ")  # ask for new password
        salt = os.urandom(16)  # make a new salt
        key = generate_key(password_provided, salt)  # generate key
        fernet = Fernet(key)  # make Fernet object
        data = "".join(password)  # get the data
        encrypted = fernet.encrypt(data.encode())  # encrypt data
        with open("passwords.txt", "wb") as file:
            file.write(salt + encrypted)  # write to file
        print("Password saved and encrypted.")

# function to read and decrypt the file
def read_info():
    password_provided = input("Enter the password to decrypt your file: ")  # ask for file password
    try:
        with open("passwords.txt", "rb") as file:
            salt = file.read(16)  # read salt
            encrypted = file.read()  # read encrypted data
        key = generate_key(password_provided, salt)  # generate key
        fernet = Fernet(key)  # make Fernet object
        decrypted = fernet.decrypt(encrypted)  # decrypt data
        print("File contents:")
        print(decrypted.decode())  # show the data
    except Exception as e:
        print("Incorrect password or error decrypting the file.")  # error message

# function to erase all passwords
def erase_info():
    user_input = input("Would you like to remove all passwords? ").lower()  # ask for confirmation
    if user_input == "yes":
        print("Removing...")
        with open("passwords.txt", "w") as file:
            file.write("")  # clear the file
        print("Passwords removed.")

# function to get the shift amount
def get_shift_amount():
    while True:
        shift = input("Shift amount: ")  # ask for shift
        if not shift.isnumeric():
            print("Must be a positive number")  # tell them it's not a number
            continue
        return int(shift)  # return the shift amount

# main loop to run the program
while True:
    modes = {
        "create password": encrypt_password,  # option to create password
        "read file": read_info,               # option to read file
        "decrypt": decrypt_password,          # option to decrypt password
        "delete file": erase_info,            # option to delete file
        "quit": quit                          # option to quit
    }
    question = "Mode: "
    get_user_input(question, modes)  # ask the user what to do
