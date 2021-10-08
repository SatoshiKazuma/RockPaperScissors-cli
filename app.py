import random

hands = {
    0:'rock',
    1:'paper',
    2:'scissor'
}

def systemPick():
    return hands.get(random.randint(0,2))
    
def rockpaperscissor(hand, syshand):
    
    if hand.lower() == 'rock':
        if syshand == 'paper':
            print('paper wins')
            return int(0)
        elif syshand == 'scissor':
            print('rock wins')
            return int(1)
        else:
            print('Draw')
    
    elif hand.lower() == 'paper':
        if syshand == 'scissor':
            print('scissor wins')
            return int(0)
        elif syshand == 'rock':
            print('paper wins')
            return int(1)
        else:
            print('Draw')
    
    elif hand.lower() == 'scissor':
        if syshand == 'rock':
            print('rock wins')
            return int(0)
        elif syshand == 'paper':
            print('scissor wins')
            return int(1)
        else:
            print('Draw')
    

print('''
Rock, Paper, Scissor!
''')
score = int(0)
systemscore = int(0)
rounds = int(input('No.of rounds: '))
for i in range(rounds):
    print(f'\nRound {i+1}')
    hand = input('Your hand: ')
    syshand = systemPick()
    
    if hand.lower() in ['rock', 'paper', 'scissor']:
        print(f'System hand: {syshand}')
        process = rockpaperscissor(hand, syshand)
        if process == 0:
            systemscore += 1
        elif process == 1:
            score += 1
            
    else:
        print(f'pick a valid hand, {hand} is not valid')

print(f'\nYour scored {score} and the system scored {systemscore}')

if score > systemscore:
    print('\nYou win')
elif score < systemscore:
    print('\nThe System wins')
else:
    print("\nIt's a draw")