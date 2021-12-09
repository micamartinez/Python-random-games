import random


def play():
    user = input('"r" for rock, "p" for paper and "s" for scissors: ')
    computer = random.choice(['r','p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if winner(user, computer):
        return 'You won!'
    
    return 'You lost!'
    
       
def winner(player, opponent):
    """Returns True if the player wins"""
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') \
       or (player == 's' and opponent == 'p') \
       or (player == 'p' and opponent == 'r'):
        return True
 

play()
