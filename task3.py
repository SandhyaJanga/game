#codesoft
import random
def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_score = 0
    user_score = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors, or quit): ").lower()
        if user_choice == "quit":
            break

        if user_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue
        #codesoft
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        #codesoft
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        #codesoft
        print(f"Score: User - {user_score}, Computer - {computer_score}\n")
        #codesoft
        print("Game over. Final score:")
        print(f"User - {user_score}, Computer - {computer_score}")

play_game()

