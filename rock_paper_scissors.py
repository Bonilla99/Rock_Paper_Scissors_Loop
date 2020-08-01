import random

options = ["rock", "paper", "scissors"]

keep_playing = "true"
while keep_playing == "true":
    pc_move = random.choice(options)
    player_move = input("What do you want to throw: rock, paper, or scissors?")
    print ("The pc chose", pc_move)
    if pc_move == player_move:
        print ("Draw!")
    elif player_move == "rock" and pc_move == "scissors":
        print("You Win!")
    elif player_move == "rock" and pc_move == "paper":
        print("You lose!")
    elif player_move == "paper" and pc_move == "rock":
        print("You Win!")
    elif player_move == "paper" and pc_move == "scissors":
        print("You Lose!")
    elif player_move == "scissors" and pc_move == "rock":
        print("You Lose!")
    elif player_move == "scissors" and pc_move == "paper":
        print("You Win!")
