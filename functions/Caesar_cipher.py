alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

def encrypt(text,shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet letter
            # Determine the case (uppercase or lowercase)
            case = ord('A') if char.isupper() else ord('a')
            # Apply the Caesar Cipher formula
            result += chr((ord(char) - case + shift) % 26 + case)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

if direction == 'encode':
    print(encrypt(text,shift))
else:
    print(encrypt(text,-shift))