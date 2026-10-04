import random
import inquirer

class Pass_Generator:
    def __init__(self, length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_special_chars = use_special_chars
        self.lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
        self.uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.number_chars = '0123456789'
        self.special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?/`~'

    def generate_password(self):
        char_pool = self.lowercase_chars
        if self.use_uppercase:
            char_pool += self.uppercase_chars
        if self.use_numbers:
            char_pool += self.number_chars
        if self.use_special_chars:
            char_pool += self.special_chars

        if not char_pool:
            raise ValueError("At least one character set must be selected")
        if self.length == 0:
            return ""

        password = ''.join(random.choice(char_pool) for _ in range(self.length))
        return password
    
if __name__ == "__main__":
    # Generate choices from 0 to 20
    length_choices = [str(i) for i in range(21)]

    questions = [
        # Arrow key selector for length
        inquirer.List(
            'length',
            message="Select the desired password length (0-20)",
            choices=length_choices,
            default="12"  # Starts the cursor at 12
        ),
        inquirer.Confirm(
            'use_uppercase', 
            message="Include uppercase letters?", 
            default=True
        ),
        inquirer.Confirm(
            'use_numbers', 
            message="Include numbers?", 
            default=True
        ),
        inquirer.Confirm(
            'use_special_chars', 
            message="Include special characters?", 
            default=True
        ),
    ]

    answers = inquirer.prompt(questions)

    if answers:
        generator = Pass_Generator(
            length=int(answers['length']), 
            use_uppercase=answers['use_uppercase'], 
            use_numbers=answers['use_numbers'], 
            use_special_chars=answers['use_special_chars']
        )
        password = generator.generate_password()
        
        if password:
            print(f"\nGenerated Password: {password}")
        else:
            print("\nGenerated Password: (Empty password because length was 0)")