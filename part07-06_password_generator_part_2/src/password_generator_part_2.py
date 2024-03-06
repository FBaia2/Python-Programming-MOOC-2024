import random
import string

def generate_strong_password(length, include_numbers, include_special_chars):
    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_chars = "!?=+-()#"

    # Start with at least one lowercase letter
    password = [random.choice(lowercase_letters)]

    # Add numbers if required
    if include_numbers:
        password.append(random.choice(numbers))

    # Add special characters if required
    if include_special_chars:
        password.append(random.choice(special_chars))

    # Fill the rest of the password length with a mix of the allowed characters
    all_allowed_chars = lowercase_letters
    if include_numbers:
        all_allowed_chars += numbers
    if include_special_chars:
        all_allowed_chars += special_chars

    while len(password) < length:
        password.append(random.choice(all_allowed_chars))

    # Shuffle the characters randomly
    random.shuffle(password)

    # Join the characters together to form the password
    password = ''.join(password)

    return password
if __name__=="__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
