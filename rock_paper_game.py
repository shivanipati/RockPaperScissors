



#rock paper scissors game

import random

def play():
    shivani = input("what choose 'r' for rock  ,'s' for scissors,'p' for paper" )
    computer = random.choice(['s','p','r'])

    # s>p,p>r,r>s

    if shivani == computer:
        return "its tie"

    if is_win(shivani,computer):
        return  " its won"
    return " its lose"

def is_win(player,opponent):
    #return true
    if (player=='s' and opponent=='p') or (player =='p' and opponent == 'r') or (player == 'r' and opponent =='s'):
        return True

print(play())