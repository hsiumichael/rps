"""Random is imported for the CPU to choose between rock, paper, and scissors."""
import random

# Variable used to keep playing the game until the player wants to stop.
game_continues = True

while game_continues == True:
    # Variable used to make sure the player types R, P, or S, not case-sensitive.
    valid_option = False
    while valid_option == False:
        player_rps = input("Type R for rock, P for paper, or S for scissors: ")
        player_rps = player_rps.upper()
        if player_rps in ("R", "P", "S"):
            valid_option = True
        else:
            print("Invalid response.")
    # The CPU randomly chooses rock, paper, or scissors.
    rps = ["rock", "paper", "scissors"]
    cpu_rps = random.choice(rps)
    # Determining win, loss, or draw.
    if player_rps == "R":
        if cpu_rps == "rock":
            print("CPU chose rock. Draw.")
        elif cpu_rps == "paper":
            print("CPU chose paper. CPU wins.")
        else:
            print("CPU chose scissors. You win!")
    elif player_rps == "P":
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
    # Y to play again, any other key to stop playing. Case-insensitive.
    # Using any other key to quit makes it so I do not need to write another while loop.
    play_again = input("Play again? Type Y to play again, any other key to quit: ")
    play_again = play_again.upper()
    if play_again != "Y":
        game_continues = False
