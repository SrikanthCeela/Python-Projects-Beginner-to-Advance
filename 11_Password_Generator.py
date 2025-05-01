import string
import random

# User inputs
num_letters = int(input("Enter number of letters: "))
num_digits = int(input("Enter number of digits: "))
num_symbols = int(input("Enter number of symbols: "))

# Character sets
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Randomly choose characters from each set
password_chars = (
    random.choices(letters, k=num_letters) +
    random.choices(digits, k=num_digits) +
    random.choices(symbols, k=num_symbols)
)

# Shuffle to avoid predictable patterns
random.shuffle(password_chars)

# Convert list to string
password = ''.join(password_chars)

print("Generated password:", password)
