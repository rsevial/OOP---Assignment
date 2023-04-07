# Programmed by: Rebekah Joy E. Sevial
# Date Programmed: 4/7/2023
# Problem 3

# Implementing keypadding method
def pad_key(message, key):
# Variable to store padded key
    padded_key = ""
# Check the chr if alpha
    i = 0
    for chr in message:
        if chr.isalpha():
            padded_key += key[i % len(key)]
            i += 1
        # Else, ignore and append as empty
        else:
            padded_key += ' '
    # Return padded_key          
    return padded_key

# Implement encrypt character method
def encrypt_char(message_char, key_char, mode='encrypt'):
# Check if the message is alpha and is an uppercase letter
    if message_char.isalpha():
        # Define as "a"
        alphabet_letter = "a"
        if message_char.isupper():
            # Define as "A"
            alphabet_letter = "A"

# Find the position of the message's char in alphabet
        old_message_position = ord(message_char) - ord(alphabet_letter)
# Find the  position of the key's char in alphabet
        key_position = ord(key_char.lower()) - ord('a')
# Find the new postion of the message 
        if mode == 'encrypt':
            new_message_position = (old_message_position + key_position) % 26
        # Return char
        return chr(new_message_position + ord(alphabet_letter))
    # If not, return message_char
    return message_char

# Implement encrypt method
def encrypt(message, key):
    encrypted = ''
    padded_key = pad_key(message, key)
    for message_char, key_char in zip(message, padded_key):
        encrypted += encrypt_char(message_char, key_char)
    return encrypted

# Ask the user to input a message and key to encrypt
message = input("Enter a message in uppercase letter with no spaces:")
key = input("Enter a keyword in uppercase letter with no spaces:")
encrypted_message = encrypt(message, key)

# Import module
import fontstyle
 
# Format massage and key
message_color = fontstyle.apply(message, 'BLUE/WHITE_BG')
encrypted_message_color = fontstyle.apply(encrypted_message, 'BLUE/WHITE_BG')

# Print the output with color
print("Original message:", message_color)
print("Encrypted message: ", encrypted_message_color)
