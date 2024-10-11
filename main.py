import random

def generate_password(length):
    if length < 1:
        return "Password length should be at least 1"


    # Define the character set manually
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!@#$%^&*()-_=+[]{}|;:,.<>?/`~'
    
    characters = lowercase + uppercase + digits + punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()

