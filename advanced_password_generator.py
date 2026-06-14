import string
import random
from collections import deque  # 1. Import the special clipboard

print('Welcome to the PyPassword Generator')

# 2. Create our 100-slot clipboard
password_history = deque(maxlen=100)

all_letters_list = list(string.ascii_letters)
all_numbers_list = list(string.digits) 
all_symbol_list = list(string.punctuation)

# 3. Put the program in a loop so it stays alive to record history
while True:
    print("\n--- Menu ---")
    print("1. Generate a Password")
    print("2. View Last 100 Passwords")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ").strip()
    
    if choice == '1':
        try:
            user_input_letters = int(input(f'Letters (1-{len(all_letters_list)}): '))
            user_input_symbols = int(input(f'Symbols (1-{len(all_symbol_list)}): '))
            user_input_numbers = int(input(f'Numbers (1-{len(all_numbers_list)}): '))

            pass_letters = random.sample(all_letters_list, user_input_letters)
            pass_symbols = random.sample(all_symbol_list, user_input_symbols)
            pass_numbers = random.sample(all_numbers_list, user_input_numbers)

            password_list = pass_letters + pass_symbols + pass_numbers
            random.shuffle(password_list)
            final_password = "".join(password_list)

            print(f'\nYour password is: {final_password}')
            
            # 4. Save the new password to our history clipboard!
            # If there are already 100, the oldest one automatically vanishes.
            password_history.append(final_password)

        except ValueError:
            print('Please enter numbers only!')
            
    elif choice == '2':
        print("\n--- Password History (Latest First) ---")
        if not password_history:
            print("No passwords generated yet.")
        else:
            # We reverse it so the newest password appears at the top of the list
            for index, pwd in enumerate(reversed(password_history), 1):
                print(f"{index}. {pwd}")
                
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please pick 1, 2, or 3.")
