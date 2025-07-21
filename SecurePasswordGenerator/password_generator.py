import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_numbers = use_numbers
        self.use_symbols = use_symbols

    def generate(self):
        char_sets = []
        if self.use_uppercase:
            char_sets.append(string.ascii_uppercase)
        if self.use_lowercase:
            char_sets.append(string.ascii_lowercase)
        if self.use_numbers:
            char_sets.append(string.digits)
        if self.use_symbols:
            char_sets.append(string.punctuation)

        if not char_sets:
            raise ValueError("At least one character set must be selected.")

        all_chars = "".join(char_sets)
        password = "".join(random.choice(all_chars) for _ in range(self.length))
        return password
