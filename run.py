import random

# Initialise scores
player_score = 0
computer_score = 0

# Welcome message and instructions
print("Welcome to rock, paper, scissors.")
print("To play, enter your choice of rock, paper, or scissors in lowercase.")
print("The computer will also choose one of the three choices.")
print("Rock smashes scissors, scissors cuts paper, and paper covers rock.")
print("The game series ends when either the user or computer wins three rounds first.")
print("After each series, you can choose to continue playing by typing yes or no, in lowercase.")

#While loop that determines the winner of the round.
while True:
    while player_score < 3 and computer_score < 3:
        computer = random.choice(['rock', 'paper', 'scissors'])
        player = input("Enter your move (rock, paper, scissors):\n ").lower()

        # Validate player's input
        while player not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            player = input("Enter your move (rock, paper, scissors): ").lower()

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Current score: You {player_score} - Computer {computer_score}")

        
    # Determine the final winner of the series
    if player_score == 2:
        print("Congratulations, you win the series!")
    elif computer_score == 2:
        print("Computer wins the series!")
    else:
        print("The series is a draw!")

# Ask the user if they want to continue playing
    play_again = input("Play again? (yes/no):\n ").lower()
    if play_again == "yes":
        player_score = 0
        computer_score = 0

# Validate player's input
    while player not in ['yes', 'no']:
        print("Invalid choice. Please enter yes or no.")
        player = input("Play again? (yes/no): ").lower()

    else:
        print("Thanks for playing!")
        break
    


