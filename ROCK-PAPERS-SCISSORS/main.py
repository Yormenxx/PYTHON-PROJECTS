import random

def play():

    user = input("'r' for rock, 'p' for paper, 's' for scissors : ")

    computer = random.choice(["r", "p", "s"])

    if(user == computer):

        return "It's a tie"

    if is_win(user,computer):
        return "User win"

    return "You lost"

def is_win(player, oppo):

    if(player =="r" and oppo =="s") or (player =="s" and oppo =="p") or (player =="p" and oppo =="r"):
        return True



print(play())