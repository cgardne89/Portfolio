# Shift Key Encryption and Decryption
import string
# Lists

Letters = list(string.ascii_uppercase)
Symbols = list(string.punctuation)
Spaces = list(string.whitespace)

# modules
def check_encryptOrDecrypt(ciphered):
    if (Encrypt_or_Decrypt) == "Decrypt":
        ciphered = ciphered - shiftKey
    elif (Encrypt_or_Decrypt) == "Encrypt":
        ciphered = ciphered + shiftKey
    return ciphered
def do_Symbol_Wrapping(ciphered):
    if (ciphered) <= 26 or (ciphered) <= 0:
        ciphered = ciphered % 27
    return ciphered 
def do_Letter_Wrapping(ciphered):
    if (ciphered) >= 25 or (ciphered) <= 0:
        ciphered = ciphered % 26
    return ciphered
def do_Number_Wrapping(ciphered):
    if (ciphered) >= 0 and (ciphered) <= 9:
        return ciphered
    if (ciphered) > 9 or (ciphered) < 0:
        ciphered = ciphered % 10
        return ciphered
def getLetters():
    charPos = Letters.index(char)
    ciphered = int(charPos)
    return ciphered
def getSymbols():
    charPos = Symbols.index(char)
    ciphered = int(charPos)
    return ciphered

while True:

    # User initial input
    Encrypt_or_Decrypt = input("Encrypt or Decrypt: ")
    Encrypt_or_Decrypt = Encrypt_or_Decrypt.capitalize()

    if (Encrypt_or_Decrypt) == "Decrypt" or (Encrypt_or_Decrypt) == "Encrypt":
        
        phrase = input("Phrase: ")
        phrase = phrase.upper()
        shiftKey = int(input("Shift: "))
        totalCiphered = []



        # Cipher Logic
        for char in phrase:

            if char in Letters:
                ciphered = getLetters()
                # check users input
                ciphered = check_encryptOrDecrypt(ciphered)
                # wrapping letters list from 0 - 25 (A - Z)
                ciphered = Letters[do_Letter_Wrapping(ciphered)]
                # add letters to a list
                totalCiphered.append(ciphered)
            elif char in Spaces:
                totalCiphered.append(char)
            elif char in Symbols:
                ciphered = getSymbols()
                # check users input
                ciphered = check_encryptOrDecrypt(ciphered)
                # wrapping symbol list 0 - 26
                ciphered = Symbols[do_Symbol_Wrapping(ciphered)]
                # add symbols to a list
                totalCiphered.append(ciphered)
            elif (char.isnumeric()):
                ciphered = int(char)
                # check for users input
                ciphered = check_encryptOrDecrypt(ciphered)
                # wrapping numbers around 1 - 9
                ciphered = do_Number_Wrapping(ciphered)
                # add numbers to a list
                totalCiphered.append(str(ciphered))

        # Result
        print("".join(totalCiphered).capitalize())
        break

    # Some error handling
    print("\033[91mError:\033[0m encrypt or decrypt")