# Shift Key Encryption and Decryption
import string
# Lists

Letters = list(string.ascii_uppercase)
Symbols = list(string.punctuation)
Spaces = list(string.whitespace)
Digits = list(string.digits)

# modules
def check_encryptOrDecrypt(ciphered, action, shiftKey):
    if action == "Decrypt":
        return ciphered - shiftKey
    elif action == "Encrypt":
        return ciphered + shiftKey
def do_Symbol_Wrapping(ciphered):
    return ciphered % len(Symbols)
def do_Letter_Wrapping(ciphered):
    return ciphered % len(Letters)
def do_Number_Wrapping(ciphered):
        return ciphered % 10
def getDigits(char):
    return int(Digits.index(char))
def getLetters(char):
    return int(Letters.index(char))
def getSymbols(char):
    return int(Symbols.index(char))

while True:

    # User initial input
    Encrypt_or_Decrypt = input("Encrypt or Decrypt: ").capitalize()

    if (Encrypt_or_Decrypt) == "Decrypt" or (Encrypt_or_Decrypt) == "Encrypt":
        
        phrase = input("Phrase: ")
        phrase = phrase.upper()
        shiftKey = int(input("Shift: "))
        totalCiphered = []



        # Cipher Logic
        for char in phrase:

            if char in Letters:
                ciphered = getLetters(char)
                # check users input
                ciphered = check_encryptOrDecrypt(ciphered, Encrypt_or_Decrypt, shiftKey)
                # wrapping letters list from 0 - 25 (A - Z)
                ciphered = Letters[do_Letter_Wrapping(ciphered)]
                # add letters to a list
                totalCiphered.append(ciphered)
            elif char in Spaces:
                totalCiphered.append(char)
            elif char in Symbols:
                ciphered = getSymbols(char)
                # check users input
                ciphered = check_encryptOrDecrypt(ciphered, Encrypt_or_Decrypt, shiftKey)
                # wrapping symbol list 0 - 26
                ciphered = Symbols[do_Symbol_Wrapping(ciphered)]
                # add symbols to a list
                totalCiphered.append(ciphered)
            elif char in Digits:
                ciphered = getDigits(char)
                # check for users input
                ciphered = check_encryptOrDecrypt(ciphered, Encrypt_or_Decrypt, shiftKey)
                # wrapping numbers around 1 - 9
                ciphered = do_Number_Wrapping(ciphered)
                # add numbers to a list
                totalCiphered.append(str(ciphered))

        # Result
        print("".join(totalCiphered).capitalize())
        break

    # Some error handling
    print("\033[91mError:\033[0m encrypt or decrypt")