import random

#initialise scores
player_score = 0
computer_score = 0

#Welcome message and instructions on how to play
print("Welcome to rock, paper, scissors.")
print("To play, the user should choose enter their choice of either rock, paper or scissors in the terminal in lowercase.")
print("The computer will also choose one of the three choices. ")
print("The rules to win are as follows: \nrock smashes scissors, \nscissors cuts paper and \npaper covers rock.")
print("The terminal will display the winner by writing the score: \n1 for the winner and \n0 for the loser at the end of each round.")
print("The game series ends when either the user or computer wins three rounds first.")
print("The user can then choose to continue playing by typing yes or no, in lowercase, when prompted. ")
print("The user can then choose to continue playing by typing yes or no, in lowercase, when prompted. If the user opts to continue playing, the game will start from the beginning.")
print("If the user opts not to continue playing, the game will exit the loop.")