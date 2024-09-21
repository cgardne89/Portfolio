# Shift Key Encryption and Decryption



Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
        "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z"]

    
while True:
    
    # User initial input
    Encrypt_or_Decrypt = input("Encrypt or Decrypt: ")
    Encrypt_or_Decrypt = Encrypt_or_Decrypt.capitalize()

    if (Encrypt_or_Decrypt) == "Decrypt" or (Encrypt_or_Decrypt) == "Encrypt":
        
        
        to_Cryption = input("Phrase: ")
        to_Cryption = to_Cryption.upper()
        shiftKey = int(input("Shift Key amount: "))

        
        totalDecrypted = []


        # Cipher Logic
        for char in to_Cryption:


            if (Letters.__contains__(char)):
                charPos = Letters.index(char)
                if (Encrypt_or_Decrypt) == "Decrypt":
                    crypted = int(charPos) - shiftKey
                if (Encrypt_or_Decrypt) == "Encrypt":
                    crypted = int(charPos) + shiftKey
                Decryption = Letters[crypted]
                totalDecrypted.append(Decryption)

            if (char.isnumeric()):
                if (Encrypt_or_Decrypt) == "Decrypt":
                    number = int(char) - shiftKey
                if (Encrypt_or_Decrypt) == "Encrypt":
                    number = int(char) + shiftKey
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

    print("\033[91mError:\033[0m encrypt or decrypt")