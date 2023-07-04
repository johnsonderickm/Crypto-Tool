import base64
from random import choice

def Base64(option):
    choice = input('\nSelect: \n1. Encode \n2. Decode\n\nYour Choice: ')
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
    
    else:
        print("1nV4L1d_cH01c3")


option = input('Select the option: \n1. Base64 \n\nYour Choice: ')
if option == '1':
    Base64(option)
else:
    print("1nV4L1d_cH01c3")
