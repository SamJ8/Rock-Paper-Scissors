import random
import time
from art import hands
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

print(Fore.YELLOW + ("""
██████   ██████   ██████ ██   ██        ██████   █████  ██████  ███████ ██████         ███████  ██████ ██ ███████ ███████  ██████  ██████  ███████ 
██   ██ ██    ██ ██      ██  ██         ██   ██ ██   ██ ██   ██ ██      ██   ██        ██      ██      ██ ██      ██      ██    ██ ██   ██ ██      
██████  ██    ██ ██      █████          ██████  ███████ ██████  █████   ██████         ███████ ██      ██ ███████ ███████ ██    ██ ██████  ███████ 
██   ██ ██    ██ ██      ██  ██         ██      ██   ██ ██      ██      ██   ██             ██ ██      ██      ██      ██ ██    ██ ██   ██      ██ 
██   ██  ██████   ██████ ██   ██ ▄█     ██      ██   ██ ██      ███████ ██   ██ ▄█     ███████  ██████ ██ ███████ ███████  ██████  ██   ██ ███████ 
                                                                                                                                                   
                                                                                                                                                   
"""))

choice = ["rock", "paper", "scissors"] ## These will be the choices we can make

def winner(player, computer):
    global player_wins, computer_wins  ## Accessing the global player_wins variable
    if player == computer:
        return("It's a tie game!\n")
    elif ((player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper")):
        player_wins += 1  ## Increments player wins
        return("You won!\n")
       
    else:
        computer_wins += 1
        return("You lost! Try again!\n")
        

playing, invalid = True, False ## variable to check if playing is either true or false
player_wins = 0
computer_wins = 0
games_played = 0
while playing: ## while loop to carry on until q is hit
    games_played = games_played+1
    if not invalid: 
        print(Fore.LIGHTCYAN_EX + "Choose Rock, Paper or Scissors")
    else:
        print(Fore.LIGHTCYAN_EX + "Invalid input, please type rock, paper or scissors") ## if invalid text is inputted, it will display invalid
    invalid = False
    print("Or press 'q' to quit\n") ## this is so user can quit
    
    player_choice = input().lower() ## user can input using this variable, will make everything lowercase

    computer_choice = random.choice(choice) ## random choice used and calling the choices from the choices list

    if player_choice in choice:
        print(Fore.GREEN + "Player chose: " + player_choice.capitalize() + hands(player_choice)) ## will display our play choice being capitalised
        print(Fore.RED + "Computer chose: " + computer_choice.capitalize() + hands(computer_choice)) ## will display computers choices being capitalised
        print(winner(player_choice, computer_choice))
        print(Fore.BLUE + "Games played:", games_played)
        print(Fore.GREEN + "Player wins:", player_wins)
        print(Fore.RED + "Computer wins:", computer_wins)

        if player_wins == 5 or computer_wins == 5:
            if player_wins == 5:
                print("Congratulations! You won the best of 5 games!")
            else:
                print("Computer won the best of 5 games! Better luck next time!")
            break  ## End the game when someone wins 5 out of 5 games
    
    elif player_choice == 'q':
        playing = False ## if player hits q, program ends ending loop

    else:
        invalid = True