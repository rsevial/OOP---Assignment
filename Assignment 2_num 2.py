# Programmed by: Rebekah Joy E. Sevial
# Date Programmed: 4/4/2023
# Problem 2

# Ask user to input string
user_str = input("Enter a string to decrypt: ")

# Adding empty list into variable text
text = []

# For loop that will replace the special characters into vowels
for signs in user_str:
    # If asterisk is inputted, replace it into an a
    if signs == "*":
        signs = "a"
    # If ampersand is inputted, replace it into an e
    elif signs == "&":
        signs = "e"
    # If hashtag is inputted, replace it into an i
    elif signs == "#":
        signs = "i"
    # If plus sign is inputted, replace it into o
    elif signs == "+":
        signs = "o"
    # If exclamation point  is inputted, replace it into u
    elif signs == "!":
        signs = "u"
    # All the text will be append
    text.append(signs)

# Creating an empty string
string = ""

# If the vowel is in the text, assign the string to the vowel
for signs in text:
    string = string + signs

# Import module
import fontstyle
 
# Format string
string_color = fontstyle.apply(string, 'BLUE/WHITE_BG')
 
# Display the string
print("The Plain Text:", string_color)
