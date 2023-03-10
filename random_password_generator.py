import random
import string

# Define the length of the password
password_length = 15

# Define the character sets to use in the password
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
numbers = string.digits
special_characters = string.punctuation

# Combine the character sets into one string
all_characters = lowercase_letters + uppercase_letters + numbers + special_characters

# Generate the password
password = ''.join(random.choice(all_characters) for i in range(password_length))

# Output the password to the user
print(f"Your random password is: {password}")
