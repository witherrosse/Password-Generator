import random
import string


def generate_password(length: int, use_symbols=True) -> str:
    """
    Generate a random password.

    Args:
        length (int): Total length of the password
        use_symbols (bool): Whether to include symbols

    Returns:
        str: Randomly generated password
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    letters = string.ascii_letters  # a-zA-Z
    digits = string.digits  # 0-9
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Ensure at least one of each category
    password_chars = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols) if use_symbols else random.choice(letters),
    ]

    # Fill the rest
    if use_symbols:
        all_chars = letters + digits + symbols
    else:
        all_chars = letters + digits

    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    # Shuffle to avoid predictable positions
    random.shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("🔑 Welcome to Password Generator!")
    try:
        length = int(input("Enter desired password length: "))
        include_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"
        password = generate_password(length, include_symbols)
        print(f"\nGenerated password: {password}")
    except ValueError as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
