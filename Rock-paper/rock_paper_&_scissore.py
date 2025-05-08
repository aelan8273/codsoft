import random

# Choices
options = ['rock', 'paper', 'scissors']

# Scores
user_score = 0
computer_score = 0

while True:
    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice. Try again.")
        continue

    # Computer choice
    computer_choice = random.choice(options)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Display score
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # Play again?
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
