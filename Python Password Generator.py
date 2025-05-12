import random
import string

def generate_password(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.coice(characters) for i in range(length))
    return password

# Example Usage
password_length = 12
print("Generated password:", generate_password(password_length))
