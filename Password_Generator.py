import string
import random

# define the characters that can be used in the password
all_characters = string.ascii_letters + string.digits + string.punctuation

# ask the user for the desired length of the password
length = int(input("Enter the length of the password: "))

password = ''.join(random.choices(all_characters, k=length))

# display the generated password to the user
print("Your password is:", password)