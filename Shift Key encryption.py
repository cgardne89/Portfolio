# Shift Key Encryption and Decryption

Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
        "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", 
           "(", ")", "-", "_", "=", "+", "[", "]", 
           "{", "}", "|", "\\", ":", ";", "\"", "'", 
           "<", ">", ",", ".", "?", "/"]



def check_encryptOrDecrypt(ciphered):
    if (Encrypt_or_Decrypt) == "Decrypt":
        ciphered = ciphered - shiftKey
    else:
        ciphered = ciphered + shiftKey

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

while True:
    
    # User initial input
    Encrypt_or_Decrypt = input("Encrypt or Decrypt: ")
    Encrypt_or_Decrypt = Encrypt_or_Decrypt.capitalize()

    if (Encrypt_or_Decrypt) == "Decrypt" or (Encrypt_or_Decrypt) == "Encrypt":
        
        phrase = input("Phrase: ")
        phrase = phrase.upper()
        shiftKey = int(input("Shift Key amount: "))

        
        totalCiphered = []


        # Cipher Logic
        for char in phrase:
            if char in Letters:
                # Function this
                charPos = Letters.index(char)
                ciphered = int(charPos)


                # create wrapping
                ciphered = check_encryptOrDecrypt(ciphered)
                ciphered = Letters[do_Letter_Wrapping(ciphered)]

                totalCiphered.append(ciphered)

            if (char.isnumeric()):
                ciphered = int(char)

                # check for users input
                ciphered = check_encryptOrDecrypt(ciphered)

                # wrapping numbers around 1 - 9
                ciphered = do_Number_Wrapping(ciphered)
                totalCiphered.append(str(ciphered))


        # Result
        print("".join(totalCiphered).capitalize())
        break

    print("\033[91mError:\033[0m encrypt or decrypt")