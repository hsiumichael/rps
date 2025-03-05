"""Random is imported for the CPU to choose between rock, paper, and scissors."""
import random

# Loop enables player(s) to play the game as many times as they want.
while True:
    # Can be played by 1 or 2 people.
    while True:
        number_of_players = input("1 or 2 players? ")
        if number_of_players in ("1", "2"):
            break
        print("Enter 1 or 2.")
    # Make sure the player types R, P, or S, not case-sensitive.
    while True:
        player1_rps = (input("Player 1, type R for rock, P for paper, or S for scissors: ")).upper()
        if player1_rps in ("R", "P", "S"):
            break
        print("Invalid response.")
    # In 1-player mode, the CPU is the opponent.
    if number_of_players == "1":
        # The CPU randomly chooses rock, paper, or scissors.
        rps = ["rock", "paper", "scissors"]
        cpu_rps = random.choice(rps)
        # Determining win, loss, or draw.
        if player1_rps == "R":
            if cpu_rps == "rock":
                print("CPU chose rock. Draw.")
            elif cpu_rps == "paper":
                print("CPU chose paper. CPU wins.")
            else:
                print("CPU chose scissors. You win!")
        elif player1_rps == "P":
            if cpu_rps == "rock":
                print("CPU chose rock. You win!")
            elif cpu_rps == "paper":
                print("CPU chose paper. Draw.")
            else:
                print("CPU chose scissors. CPU wins.")
        else:
            if cpu_rps == "rock":
                print("CPU chose rock. CPU wins.")
            elif cpu_rps == "paper":
                print("CPU chose paper. You win!")
            else:
                print("CPU chose scissors. Draw." )
    # In 2-player mode, use the same method as player 1 to obtain player 2's choice.
    else:
        while True:
            player2_rps = (input("Player 2, type R for rock, P for paper, or S for scissors: ")).upper()
            if player2_rps in ("R", "P", "S"):
                break
            print("Invalid response.")
        # Show both player's choices.
        if player1_rps == "R":
            print("Player 1: rock")
        elif player1_rps == "P":
            print("Player 1: paper")
        else:
            print("Player 1: scissors")
        if player2_rps == "R":
            print("Player 2: rock")
        elif player2_rps == "P":
            print("Player 2: paper")
        else:
            print("Player 2: scissors")
        # Determine the winner.
        if player1_rps == player2_rps:
            print("Draw.")
        elif (player1_rps == "R" and player2_rps == "S") or (player1_rps == "P" and player2_rps == "R") or (player1_rps == "S" and player2_rps == "P"):
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    # Y to play again, any other key to stop playing. Case-insensitive.
    play_again = input("Play again? Type Y to play again, any other key to quit: ")
    play_again = play_again.upper()
    if play_again != "Y":
        break
