import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars
    length = max(length, 4)
    password = random.sample(all_chars, length)
    password += random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(special_chars)
    random.shuffle(password)

    # Convert the list of characters to a string
    password = ''.join(password)

    return password
generated_password = generate_password()
print("Generated Password:", generated_password)
