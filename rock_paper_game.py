# import random
#
# def game():
#     user = input("what choose 'r' for rock , 'p'for paper,'s' for scissors \n")
#     computer  =random.choice(['r','p','s'])
#
#     if computer == user:
#         return  "it's tie"
#
#     #r > s, s>p , p>r
#     if is_win(user , computer):
#         return "its won!"
#     return "its lose"
#
# def is_win(player,opponent):
#     #return true
#
#     if (player == 'r'and opponent == 's') or (player == 's' and opponent == 'p')or (player=='p' and opponent=='r'):
#         return  True
#
# print(game())



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