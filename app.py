import csv, random

class rockpaperscissorsgame:
    def __init__(self,rounds) -> None:
        self.rounds = rounds
    
    def play(self):
        '''Starts a game of rock paper scissors'''
        userscore = int(0)
        systemscore = int(0)
        for i in range(0,self.rounds):
            with open('winloss.csv','r') as winloss:
                reader = csv.DictReader(winloss)
                syschoice = ['rock','paper','scissor']
                syspick = random.choice(syschoice)
                accept = False
                while not accept:
                    userpick = input('\nuserpick: ').lower()
                    print(f'systempick: {syspick}')
                    for row in reader:
                        if row['user'] == userpick and row['system'] == syspick:
                            # print(row['usrres'],row['sysres'])
                            if row['sysres'] == str(1):
                                print('system wins')
                                systemscore += 1
                            elif row['usrres'] == str(1):
                                print('user wins')
                                userscore += 1
                            elif row['sysres'] == str(2):
                                print('Tie')
                            else:
                                print('''This was not supposed to happen.
                                But i'm sure we can figure something out by ourselves, 
                                This is, afterall, an attempt to waste some more of our
                                time.''')
                            # print(f'user score is {userscore}')
                            break
                        accept = True
                    else:
                        accept = False
                        print('please pick valid input')
        print(f'\nsystemscore: {systemscore}\nuserscore: {userscore}\n')
        if userscore > systemscore:
            print('user wins')
        elif systemscore > userscore:
            print('system wins')
        elif systemscore == userscore:
            print('Ties')
try:
    game1 = rockpaperscissorsgame(3)
    game1.play()
except KeyboardInterrupt:
    print('\nGame terminated')
    