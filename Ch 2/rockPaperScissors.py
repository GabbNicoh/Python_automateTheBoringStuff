# this is my solution
import random, sys

print('ROCK, PAPER, SCISSORS')
wins = 0
loss = 0
ties = 0
while True:
    print(str(wins) + ' Wins, ' + str(loss) + ' Losses, ' + str(ties) + ' ties, ')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    move = input()
    randMov = random.randint(0,3)

    if randMov == 0: compMove = 'Rock'
    elif randMov == 1: compMove = 'Paper'
    else: compMove = 'Scissors'

    if move == 'r' or move == 'R':
        plyMove = 'Rock'
        print('Rock versus...')
    elif move == 'p' or move == 'P':
        plyMove = 'Paper'
        print('Paper versus...')
    elif move == 's' or move == 'S':
        plyMove = 'Scissors'
        print('Scissors versus...')
    elif move == 'q' or move == 'Q':
        sys.exit()
    else:
        print('Please input a r, p, s or q\n')
        continue

    print(compMove)

    if plyMove == compMove:
        print('It is a tie!')
        ties+=1
    elif plyMove == 'Rock' and compMove == 'Scissors':
        print('You win!')
        wins+=1
    elif plyMove == 'Rock' and compMove == 'Paper':
        print('You lose!')
        loss+=1
    elif plyMove == 'Paper' and compMove == 'Rock':
        print('You win!')
        wins+=1
    elif plyMove == 'Paper' and compMove == 'Scissors':
        print('You lose!')
        loss+=1
    elif plyMove == 'Scissors' and compMove == 'Paper':
        print('You win!')
        wins+=1
    elif plyMove == 'Scissors' and compMove == 'Rock':
        print('You lose!')
        loss+=1

# this is the solution of the book
import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
