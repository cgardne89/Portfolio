# Shift Key Encryption and Decryption
    
    
while True:
    
    # User initial input
    Encrypt_or_Decrypt = input("Encrypt or Decrypt: ")
    Encrypt_or_Decrypt = Encrypt_or_Decrypt.capitalize()

    if (Encrypt_or_Decrypt) == "Decrypt":
        
        
        to_Decrypt = input("What to decrypt: ")
        to_Decrypt = to_Decrypt.upper()
        shiftKey = int(input("Shift Key amount: "))

        
        totalDecrypted = []


        # Cipher Logic
        for char in to_Decrypt:

            Letter_to_Decrypt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                    "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                    "S", "T", "U", "V", "W", "X", "Y", "Z"]
            if (Letter_to_Decrypt.__contains__(char)):
                charPos = Letter_to_Decrypt.index(char)

                Decrypted = int(charPos) - shiftKey
                Decryption = Letter_to_Decrypt[Decrypted]
                totalDecrypted.append(Decryption)

            if (char.isnumeric()):
                number = int(char) - shiftKey
                if (number) > 0 and (number) < 10:
                    totalDecrypted.append(str(number))
                if (number) == 0:
                    number = number + 9
                    totalDecrypted.append(str(number))
                elif (number) >= 10 or (number) <= -1:
                    number = number % 9
                    totalDecrypted.append(str(number))


        # Result
        print("".join(totalDecrypted))
        break



    if (Encrypt_or_Decrypt) == "Encrypt":
        
        
        to_Encrypt = input("What to encrypt: ")
        to_Encrypt = to_Encrypt.upper()
        shiftKey = int(input("Shift Key amount: "))

        
        
        totalEncrypted = []

        # Cipher Logic
        for char in to_Encrypt:
            
            Letter_to_Encrypt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                    "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                    "S", "T", "U", "V", "W", "X", "Y", "Z"]
            
            if (Letter_to_Encrypt.__contains__(char)):
                charPos = Letter_to_Encrypt.index(char)
                Encrypted = shiftKey + int(charPos)
                Encryption = Letter_to_Encrypt[Encrypted]
                totalEncrypted.append(Encryption)

            if (char.isnumeric()):
                number = int(char) + shiftKey
                if (number) < 10:
                    totalEncrypted.append(str(number))
                if (number) >= 10: 
                    number = number % 9
                    totalEncrypted.append(str(number))
                
        # Result
        print("".join(totalEncrypted))
        break

    print("\033[91mError:\033[0m encrypt or decrypt")