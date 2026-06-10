import string
import random

print('Welcome to the PyPassword Generator')

# 1. Setup our ingredient bowls (Notice string.digits for 0-9)
all_letters_list = list(string.ascii_letters)
all_numbers_list = list(string.digits) # Contains ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_symbol_list = list(string.punctuation)

try:
    user_input_letters = int(input(f'How Many Letters? (1 to {len(all_letters_list)}): \n'))
    user_input_symbols = int(input(f'How Many symbols? (1 to {len(all_symbol_list)}): \n'))
    user_input_numbers = int(input(f'How Many numbers? (1 to {len(all_numbers_list)}): \n'))

    # FIX: Matching the right list with the right user input
    pass_letters = random.sample(all_letters_list, user_input_letters)
    pass_symbols = random.sample(all_symbol_list, user_input_symbols)
    pass_numbers = random.sample(all_numbers_list, user_input_numbers)

    # Combine them all into one big list of characters
    password_list = pass_letters + pass_symbols + pass_numbers
    
    # Optional but highly recommended: Shuffle them so the order is random!
    random.shuffle(password_list)

    # Turn the list back into a clean string text
    final_password = "".join(password_list)

    print(f'Your password is: {final_password}')

except ValueError:
    print('Please enter numbers only!')
