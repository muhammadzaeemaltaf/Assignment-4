from random import choice

def play():
    user = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return "You win!"
    
    return "You lose!"

# r > s, p > r, s > p
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    


if __name__ == "__main__":
    print(play())