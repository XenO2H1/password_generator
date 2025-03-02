import random
import string

def generate_password(length=8, use_uppercase=True, use_numbers=True, use_special=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''

    all_characters = lowercase + uppercase + digits + special

    if not all_characters:
        print("Please select at least one character set.")
        return None

    password = ''.join(random.choice(all_characters) for _ in range(length))
    print("Password Strength:", check_password_strength(password))  # Show strength automatically
    return password

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if length < 6:
        return "Weak 😴"
    elif length >= 6 and length <= 10 and (has_digit or has_upper):
        return "Medium ⚡"
    elif length > 10 and has_upper and has_digit and has_special:
        return "Strong 🔥"
    else:
        return "Medium ⚡"

if __name__ == "__main__":
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_special)
    if password:
        print("Generated Password:", password)

