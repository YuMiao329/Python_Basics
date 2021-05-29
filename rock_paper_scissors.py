import random

choices = ['rock','paper','scissor']
play_again = 'y'
while play_again == 'y':
    computer = random.choice(choices)
    player = None
    while player not in (choices):
        player = input('rock,paper,scissor?: ').lower()
    if player == computer:
        print('computer: '+computer)
        print('player: '+player)
        print('Tie!')
    elif player == 'rock' and computer == 'scissor':
        print('computer: '+computer)
        print('player: '+player)
        print('You Win!')
    elif player == 'rock' and computer == 'paper':
        print('computer: '+computer)
        print('player: '+player)
        print('You Lose!')
    elif player == 'scissor' and computer == 'rock':
        print('computer: '+computer)
        print('player: '+player)
        print('You Lose!')
    elif player == 'scissor' and computer == 'paper':
        print('computer: '+computer)
        print('player: '+player)
        print('You Win')
    elif player == 'paper' and computer == 'scissor':
        print('computer: '+computer)
        print('player: '+player)
        print('You Lose!')
    elif player == 'paper' and computer == 'rock':
        print('computer: '+computer)
        print('player: '+player)
        print('You Win')

    play_again = input('Again?: (y/n)').lower()

    if play_again != 'y':
        break
print('Bye!')