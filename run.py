import random
from colorama import Fore, Back, Style


def welcome():
    """
    Welcome message and instructions
    """
    print(Fore.CYAN + "Welcome to rock, paper, scissors.")
    print(
        "To play, enter your choice of rock, paper, or scissors in lowercase."
    )
    print(
        "The computer will also choose one of the three choices."
    )
    print(
        "Rock smashes scissors, scissors cuts paper, and paper covers rock."
    )
    print(
        "The game series ends when the user or computer wins three rounds."
    )
    print(
        "After each series, you can choose to continue playing."
    )
    print(
        "Type yes or no, in lowercase, to do this."
    )
    print(Style.RESET_ALL)
    game()


def game():
    """
    This function starts the game and prompts the user to enter an option.
    The computer also enters a random option.
    The winner of the round is determined based on the rules above.
    The first to win 3 rounds wins the series.
    The user is asked to continue the game or not.
    """

    player_score = 0
    computer_score = 0
    # Initialisea scores
    while True:
        # While loop that determines the winner of the round.
        while player_score < 3 and computer_score < 3:
            computer = random.choice(['rock', 'paper', 'scissors'])
            player = input(
                Fore.BLUE +
                "Enter your move (rock 🪨 , paper 🗒 ,"
                "scissors ✂ ):\n "
                )
            print(Style.RESET_ALL)

            # Validate player's input
            while player not in ['rock', 'paper', 'scissors']:
                print(
                    Fore.RED +
                    "Invalid choice. Please enter rock 🪨 , paper 🗒 ,"
                    "or scissors ✂ ."
                    )
                print(Style.RESET_ALL)
                player = input(
                    "Enter your move (rock 🪨 , paper 🗒 ,"
                    "scissors ✂ ): "
                    )

            if player == computer:
                print(Fore.MAGENTA + "It's a tie.")
                print(Style.RESET_ALL)
            elif ((
                player == "rock" and computer == "scissors") or (
                    player == "paper" and computer == "rock") or (
                        player == "scissors" and computer == "paper"
                        )):
                print(Fore.GREEN + "You win.")
                print(Style.RESET_ALL)
                player_score += 1
            else:
                print(Fore.RED + "You lose.")
                print(Style.RESET_ALL)
                computer_score += 1

            print(
                f"Current score: You {player_score} - "
                f"Computer {computer_score}"
                )

        # Determine the final winner of the series
        if player_score == 3:
            print(Fore.GREEN + "Congratulations, you win the series! 🎉 ")
            print(Style.RESET_ALL)
        elif computer_score == 3:
            print(Fore.RED + "Computer wins the series! 🥲 ")
            print(Style.RESET_ALL)
        else:
            print(Fore.CYAN + "The series is a draw! 👏 ")
            print(Style.RESET_ALL)

        # Ask the user if they want to continue playing
        play_again = input(Fore.BLUE + "Play again? (yes/no):\n ").lower()
        print(Style.RESET_ALL)
        while play_again not in ['yes', 'no']:
            print(Fore.RED + "Invalid choice. Please enter yes or no.")
            print(Style.RESET_ALL)
            play_again = input(Fore.BLUE + "Play again? (yes/no): \n").lower()
            print(Style.RESET_ALL)

        if play_again == "yes":
            player_score = 0
            computer_score = 0
        else:
            print(Fore.GREEN + "Thanks for playing! 👋 ")
            print(Style.RESET_ALL)
            break


if __name__ == '__main__':
    welcome()
