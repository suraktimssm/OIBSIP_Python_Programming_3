import random
import string

def password_generate(length, letters, digits, symbols):
    characters = ""
    
    if letters:
        characters += string.ascii_letters
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
        
    if not characters:
        return "You must choose at least one character type!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter password length: "))
    
    if length <= 0:
        print("Password length must be a positive number.")
    else:
        letters = input("Include letters? (y/n): ").lower() == "y"
        digits = input("Include digits? (y/n): ").lower() == "y"
        symbols = input("Include symbols? (y/n): ").lower() == "y"
        
        password = password_generate(length, letters, digits, symbols)
        print(f"\nGenerated Password: {password}")
        
except ValueError:
    print("Invalid input. Please enter numbers only.")