import random

# Function to generate random password
def generate_password(length):
    # Define all possible characters to be used in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?`~"
    # Use random.sample to randomly select length number of characters from the list of characters
    password = "".join(random.sample(characters, length))
    return password

# Prompt user to choose password length
length = int(input("Please enter the desired password length: "))
# Generate password
password = generate_password(length)
# Print the generated password
print("Your randomly generated password is:", password)
