import base64

#base64 code
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


#Caeser Cipher Code
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


#Atbash Code
def Atbash(choice):
    if choice  == '1' or choice == '2':
        lookup_dict = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
            'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
            'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
            'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
            'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A', 
            'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v',
            'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q',
            'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l',
            'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g',
            'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a',
            '?' : '/', '/' : '?', '<' : '>', '>' : '<', '-' : '_', 
            '_' : '-', '!' : '@', '@' : '!', '#' : '$', '$' : '#',
            '%' : '^', '^' : '%', '&' : '*', '*' : '&', '(' : ')',
            ')' : '(', '1' : '0', '2' : '9', '3' : '8', '4' : '7',
            '5' : '6', '6' : '5', '7' : '4', '8' : '3', '9' : '2', '0' : '1'}

        message = input('\nEnter your message: ')
        decoded = ''

        for letter in message:
            if (letter != ' '):
                decoded += lookup_dict[letter]
        
            else:
                decoded += ' '
        
        print(decoded)
    
    else:
        print("1nV4L1d_cH01c3")



#driver code
while True:
    option = input('\n\nSelect the option: \n1. Base64 \n2. Ceaser Cipher \n3. Atbash Cipher \n\nYour Choice: ')
    choice = input('\nSelect: \n1. Encode \n2. Decode \n3. Main Menu \n\nYour Choice: ')
    
    if option == '1':
        print("---------- BASE 64 ----------")
        Base64(choice)
    
    elif option == '2':
        print("---------- CAESER CIPHER ----------")
        Caeser(choice)

    elif option == '3':
        print("---------- ATBASH CIPHER ----------")
        Atbash(choice)
   
    else:
        print("1nV4L1d_cH01c3")
