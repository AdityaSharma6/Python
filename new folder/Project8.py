# **********************************************************
# Assignment: Project 8: Rock Paper Scissors
# Description: 
#
# Author: Aditya Sharma
#
# Date Start: (2018/08/12)
# Date Completed: (2018/08/12)
#
# Completion time: 7:40 hours
#
# Honor Code: I pledge that this program represents my own
#   program code. I received help from (enter the names of
#   others that helped with the assignment; write no one if
#   you received no help) in designing and debugging my program.
# *********************************************************

print ("This is a Rock Paper Scissors game. You can only select, \"Rock\", \"Paper\" or \"Scissors\"")
print ("You will be playing against another person.")

player1_response = input ("Player 1, would you like to play? ").lower()
player2_response = input ("Player 2, would you like to play? ").lower()

if player1_response == "yes":
    player1_response = True

else:
    player1_response = False

if player2_response == "yes":
    player2_response = True

else:
    player2_response = False

while player1_response and player2_response:

    break




'''
while player1_response == player2_response or winner_response == loser_response:

    player1_input = input ("Player 1, what is your move? ").lower()
    player2_input = input ("Player 2, what is your move? ").lower()

    if player1_input == "rock" and player2_input == "rock":
        print (f"TIE! Player 1 picked {player1_input} and Player 2 picked {player2_input}")
        player1_response = input ("Player 1, would you like to play again? ").lower()
        player2_response = input ("Player 2, would you like to play again? ").lower()
        
        if player1_response == player2_response:
            continue
        else: 
            break


    winner_response = input ("Congratulations Winner! Would you like to play again? ")
    loser_response = input ("That battle was well-fought. Would you like a rematch? ")
'''


