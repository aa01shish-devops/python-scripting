import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Group arts into a list for easy access via index numbers 0, 1, 2
game_images = [rock, paper, scissors]

# 1. Convert input to an integer immediately
user_choice = int(input('Press: [0] for Rock, [1] for Paper, [2] for Scissors\n'))

# Optional validation: Stop the program if the user types an invalid number
if user_choice >= 3 or user_choice < 0:
    print("Invalid number! You lose by default.")
else:
    # Print user choice art
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    
    # Print computer choice art
    print("Computer chose:")
    print(game_images[computer_choice])

    # 2. Check for game rules using structural if-elif-else logic
    if user_choice == computer_choice:
        print("It's a draw!!")
    elif user_choice == 0 and computer_choice == 2:
        print("You Win!!")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win!!")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win!!")
    else:
        print("You lose!!")
