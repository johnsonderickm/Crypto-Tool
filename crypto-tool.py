import base64

def Base64(choice):
    if choice == "1":
        message = input('Enter the Plain Text: ')
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
    
        print(base64_message)

    elif choice == '2':
        base64_messaged = input('Enter the Cipher Text: ')
        base64d_bytes = base64_messaged.encode('ascii')
        messaged_bytes = base64.b64decode(base64d_bytes)
        messaged = messaged_bytes.decode('ascii')

        print(messaged)
        
    #elif choice == 3:

    else:
        print("1nV4L1d_cH01c3")



def Caeser(choice):
    if choice == '1':
        ct = " "
        pt = input("Enter the Plain Text: ")
        key = int(input('Enter the Shift Key: '))
        for i in range(len(pt)):
            char = pt[i]

            if (char.isupper()):
                ct += chr((ord(char) + key - 65) % 26 + 65)
            
            else:
                ct += chr((ord(char) + key - 97) % 26 + 97)

        print(ct)
    
    elif choice == '2':
        def caesar_decrypt(ciphertext, shift):
            pt = ""
            for char in ciphertext:
                if char.isalpha():
                    ascii_offset = ord('a') if char.islower() else ord('A')
                    decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                    pt += decrypted_char
                else:
                    pt += char
            return pt

        ciphertext = input("Enter the ciphertext: ")

        print("Brute force decryption:")
        for shift in range(26):
            decrypted_text = caesar_decrypt(ciphertext, shift)
            print(f"Shift = {shift:2}: {decrypted_text}")



#driver code
while True:
    option = input('\n\nSelect the option: \n1. Base64 \n2. Ceaser Cipher \n\nYour Choice: ')
    choice = input('\nSelect: \n1. Encode \n2. Decode \n3. Main Menu \n\nYour Choice: ')
    
    if option == '1':
        Base64(choice)
    
    elif option == '2':
        Caeser(choice)
   
    else:
        print("1nV4L1d_cH01c3")
