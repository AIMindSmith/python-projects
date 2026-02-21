# Import the random module for generating random choices
import random
# Import the string module to access character sets (letters, digits, etc.)
import string


def generate_password(min_length,numbers =True ,special_characters = True):
    # Get all lowercase and uppercase letters from the string module
    letters = string.ascii_letters
    # Get all digit characters (0-9)
    digits = string.digits
    # Get all special/punctuation characters
    some_special_characters = string.punctuation

    # Start with letters as the base character set
    CHAR = letters
    # If numbers are required, add digits to the character set
    if numbers:
        CHAR += digits
    # If special characters are required, add them to the character set
    if special_characters:
        CHAR += some_special_characters

    # Initialize the password as an empty string
    password = " "
    # Flag to check if the password meets all requirements
    Mc = False
    # Flag to track if the password has at least one number
    have_numbers = False
    # Flag to track if the password has at least one special character
    have_special_characters = False

    # Loop until password meets length requirement and contains required character types
    while not Mc or len(password) < min_length:
        # Select a random character from the available character set
        new_char = random.choice(CHAR)
        # Add the random character to the password
        password += new_char

        # Check if the selected character is a digit
        if new_char in digits:
            # Mark that the password now contains at least one number
            have_numbers = True
        # Check if the selected character is a special character
        elif new_char in some_special_characters:
            # Mark that the password now contains at least one special character
            have_special_characters = True

        # Assume password requirements are met
        Mc = True
        # If numbers are required, check if password actually has numbers
        if numbers:
            Mc = have_numbers
        # If special characters are required, check if password has both required elements
        if special_characters:
            Mc = Mc and have_special_characters

    # Return the generated password
    return password

# Get the desired password length from the user
length_of_password = int(input("Enter your desired password length: "))
# Ask user if they want numbers included, convert yes/no response to boolean
have_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
# Ask user if they want special characters included, convert yes/no response to boolean
have_special_characters = input("Include special characters? (yes/no): ").lower() == "yes"

# Call the function to generate a password with user's specifications
password = generate_password(length_of_password, have_numbers, have_special_characters)
# Display the generated password to the user
print(password)
