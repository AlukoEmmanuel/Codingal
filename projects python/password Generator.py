import random
import string

def generate_password(length, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, use_special_chars)
    print(f"Generated password: {password}")