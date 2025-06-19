import random
import string

def generate_password(length):
    # Define the character pool: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Ask the user for desired password length
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive number.")
        else:
            password = generate_password(length)
            print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()