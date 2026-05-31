import random

# Game assets
game_images = ["ROCK_ART", "PAPER_ART", "SCISSORS_ART"]
results = ["It's a draw!!", "You Win!!", "You lose!!"]

# Initialize score variables
user_score = 0
computer_score = 0
draw_count = 0

print("Welcome to Rock, Paper, Scissors!")
print("Type 'q' at any time to quit and see final scores.\n")

# This loop keeps the game running until the user types 'q'
while True:
    # Display current standings
    print(f"--- SCOREBOARD: You [{user_score}] | Computer [{computer_score}] | Draws [{draw_count}] ---")
    
    user_input = input('Press: [0] Rock, [1] Paper, [2] Scissors (or "q" to quit):\n').lower().strip()
    
    if user_input == 'q':
        print("\nThanks for playing!")
        break
        
    # Validate that the input is a valid number choice
    if user_input not in ['0', '1', '2']:
        print("Invalid choice! Please enter 0, 1, 2, or q.\n")
        continue
    
    # Convert validated string input to integer
    user_choice = int(user_input)
    computer_choice = random.randint(0, 2)
    
    print(f"\nYou chose:\n{game_images[user_choice]}")
    print(f"Computer chose:\n{game_images[computer_choice]}")
    
    # Calculate outcome instantly using the modulo wheel
    outcome = (user_choice - computer_choice) % 3
    print(results[outcome])
    
    # Update the score tracker based on the mathematical outcome
    if outcome == 1:
        user_score += 1
    elif outcome == 2:
        computer_score += 1
    else:
        draw_count += 1
        
    print("\n" + "="*40 + "\n")

# Final game summary screen
print("\n=== FINAL GAME OVER SUMMARY ===")
print(f"Total Wins: {user_score}")
print(f"Total Losses: {computer_score}")
print(f"Total Draws: {draw_count}")

if user_score > computer_score:
    print("🏆 Congratulations! You beat the computer overall!")
elif user_score < computer_score:
    print("🤖 The computer wins this session. Better luck next time!")
else:
    print("🤝 It's a complete tie overall!")
