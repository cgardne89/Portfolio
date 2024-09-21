# Shift Key Encryption and Decryption



Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
        "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z"]

    
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
                if (Encrypt_or_Decrypt) == "Decrypt":
                    ciphered = int(charPos) - shiftKey
                if (Encrypt_or_Decrypt) == "Encrypt":
                    ciphered = int(charPos) + shiftKey
                    
                # Function this
                getCiph = Letters[ciphered]
                totalCiphered.append(getCiph)

            if (char.isnumeric()):

                # Function this
                if (Encrypt_or_Decrypt) == "Decrypt":
                    number = int(char) - shiftKey
                if (Encrypt_or_Decrypt) == "Encrypt":
                    number = int(char) + shiftKey

                # function this
                if (number) > 0 and (number) < 10:
                    totalCiphered.append(str(number))
                if (number) == 0:
                    number = number + 9
                    totalCiphered.append(str(number))
                elif (number) >= 10 or (number) <= -1:
                    number = number % 9
                    totalCiphered.append(str(number))


        # Result
        print("".join(totalCiphered).capitalize())
        break

    print("\033[91mError:\033[0m encrypt or decrypt")