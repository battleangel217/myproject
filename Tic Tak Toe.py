#A game of tic tak toe

import random

class Tik_Tak_Toe:
    def __init__(self, choice = 0, player1 = '', player2 = '', row1 = [' ', '|', ' ', '|', ' '], row2 = [' ', '|', ' ', '|', ' '], row3 = [' ', '|', ' ', '|', ' ']):
        self.player1 = player1
        self.player2 = player2
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.choice = choice


    def player2_turn(self):
        player_choice = int(input('\nPlayer2(o): '))
        
        if player_choice  == 1:
            if self.row1[0] == 'x' or self.row1[0] == 'o':
                print('Space already taken')
                ttt.player2_turn()
            self.row1[0] = 'o'
        elif player_choice == 2:
            if self.row1[2] == 'x' or self.row1[2] == 'o':
                print('Space already taken')
                ttt.player2_turn()
            self.row1[2] = 'o'
        elif player_choice == 3:
            if self.row1[4] == 'x' or self.row1[4] == 'o':
                print('Space already taken')
                ttt.player2_turn()
            self.row1[4] = 'o'
        elif player_choice == 4:
            if self.row2[0] == 'x' or self.row2[0] == 'o':
                print('Space already taken')
                ttt.player2_turn()
            self.row2[0] = 'o'
        elif player_choice == 5:
            if self.row2[2] == 'x' or self.row2[2] == 'o':
                print('Space already taken')
                ttt.player2_turn()
            self.row2[2] = 'o'
        elif player_choice == 6:
            if self.row2[4] == 'x' or self.row2[4] == 'o':  
                print('Space already taken')
                ttt.player2_turn()
            self.row2[4] = 'o'
        elif player_choice == 7:
            if self.row3[0] == 'x' or self.row3[0] == 'o':
                print('Space already taken')
                ttt.player2_turn()
            self.row3[0] = 'o'
        elif player_choice == 8:
            if self.row3[2] == 'x' or self.row3[2] == 'o':
                print('Space already taken')
                ttt.player2_turn()
            self.row3[2] = 'o'
        elif player_choice == 9:
            if self.row3[4] == 'x' or self.row3[4] == 'o':
                print('Space already taken')
                ttt.player2_turn()
            self.row3[4] = 'o'
        else:
            print('Invalid number in rows')
            ttt.game_start()
        print(''.join(self.row1))
        print(''.join(self.row2))
        print(''.join(self.row3))

        if self.row1[0] == 'o' and self.row1[2] == 'o' and self.row1[4] == 'o':
            print(f'{self.player2} wins!')
            exit()
        elif self.row2[0] == 'o' and self.row2[2] == 'o' and self.row2[4] == 'o':
            print(f'{self.player2} wins!')
            exit()
        elif self.row3[0] == 'o' and self.row3[2] == 'o' and self.row3[4] == 'o':
            print(f'{self.player2} wins!')
            exit()
        elif self.row1[0] == 'o' and self.row2[0] == 'o' and self.row3[0] == 'o':
            print(f'{self.player2} wins!')
            exit()
        elif self.row1[2] == 'o' and self.row2[2] == 'o' and self.row3[2] == 'o':
            print(f'{self.player2} wins!')
            exit()
        elif self.row1[4] == 'o' and self.row2[4] == 'o' and self.row3[4] == 'o':
            print(f'{self.player2} wins!')
            exit()
        elif self.row1[0] == 'o' and self.row2[2] == 'o' and self.row3[4] == 'o':
            print(f'{self.player2} wins!')
            exit()
        elif self.row1[4] == 'o' and self.row2[2] == 'o' and self.row3[0] == 'o':
            print(f'{self.player2} wins!')
            exit()
        if self.choice == 1:
            ttt.player1_turn()
        elif self.choice == 2:
            ttt.ai()
            

    def player1_turn(self):
        player_choice = int(input('\nPlayer1(x): '))
        if player_choice  == 1:
            if self.row1[0] == 'x' or self.row1[0] == 'o':
                print('Space already taken')
                ttt.player1_turn()
            self.row1[0] = 'x'
        elif player_choice == 2:
            if self.row1[2] == 'x' or self.row1[2] == 'o':
                print('Space already taken')
                ttt.player1_turn()
            self.row1[2] = 'x'
        elif player_choice == 3:
            if self.row1[4] == 'x' or self.row1[4] == 'o':
                print('Space already taken')
                ttt.player1_turn()
            self.row1[4] = 'x'
        elif player_choice == 4:
            if self.row2[0] == 'x' or self.row2[0] == 'o':
                print('Space already taken')
                ttt.player1_turn()
            self.row2[0] = 'x'
        elif player_choice == 5:
            if self.row2[2] == 'x' or self.row2[2] == 'o':
                print('Space already taken')
                ttt.player1_turn()
            self.row2[2] = 'x'
        elif player_choice == 6:
            if self.row2[4] == 'x' or self.row2[4] == 'o':
                print('Space already taken')
                ttt.player1_turn()
            self.row2[4] = 'x'
        elif player_choice == 7:
            if self.row3[0] == 'x' or self.row3[0] == 'o':
                print('Space already taken')
                ttt.player1_turn()
            self.row3[0] = 'x'
        elif player_choice == 8:
            if self.row3[2] == 'x' or self.row3[2] == 'o':
                print('Space already taken')
                ttt.player1_turn()
            self.row3[2] = 'x'
        elif player_choice == 9:
            if self.row3[4] == 'x' or self.row3[4] == 'o':
                print('Space already taken')
                ttt.player1_turn()
            self.row3[4] = 'x'
        else:
            print('Invalid number in rows')
            ttt.game_start()
        print(''.join(self.row1))
        print(''.join(self.row2))
        print(''.join(self.row3))

        if self.row1[0] == 'x' and self.row1[2] == 'x' and self.row1[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row2[0] == 'x' and self.row2[2] == 'x' and self.row2[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row3[0] == 'x' and self.row3[2] == 'x' and self.row3[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[0] == 'x' and self.row2[0] == 'x' and self.row3[0] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[2] == 'x' and self.row2[2] == 'x' and self.row3[2] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[4] == 'x' and self.row2[4] == 'x' and self.row3[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[0] == 'x' and self.row2[2] == 'x' and self.row3[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[4] == 'x' and self.row2[2] == 'x' and self.row3[0] == 'x':
            print(f'{self.player1} wins!')
            exit()
        if self.choice == 1:
            ttt.player2_turn()
        elif self.choice == 2:
            ttt.ai()
    

    def ai(self):
        ai_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ai_choice = random.choice(ai_choices)
        print(f'\nAI(o): {ai_choice}')
        if ai_choice  == 1:
            ai_choices.remove(1)
            self.row1[0] = 'o'
        elif ai_choice == 2:
            ai_choices.remove(2)
            self.row1[2] = 'o'
        elif ai_choice == 3:
            ai_choices.remove(3)
            self.row1[4] = 'o'
        elif ai_choice == 4:
            ai_choices.remove(4)
            self.row2[0] = 'o'
        elif ai_choice == 5:
            ai_choices.remove(5)
            self.row2[2] = 'o'
        elif ai_choice == 6:
            ai_choices.remove(6)
            self.row2[4] = 'o'
        elif ai_choice == 7:
            ai_choices.remove(7)
            self.row3[0] = 'o'
        elif ai_choice == 8:
            ai_choices.remove(8)
            self.row3[2] = 'o'
        elif ai_choice == 9:
            ai_choices.remove(9)
            self.row3[4] = 'o'
        print(''.join(self.row1))
        print(''.join(self.row2))
        print(''.join(self.row3))

        if self.row1[0] == 'x' and self.row1[2] == 'x' and self.row1[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row2[0] == 'x' and self.row2[2] == 'x' and self.row2[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row3[0] == 'x' and self.row3[2] == 'x' and self.row3[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[0] == 'x' and self.row2[0] == 'x' and self.row3[0] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[2] == 'x' and self.row2[2] == 'x' and self.row3[2] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[4] == 'x' and self.row2[4] == 'x' and self.row3[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[0] == 'x' and self.row2[2] == 'x' and self.row3[4] == 'x':
            print(f'{self.player1} wins!')
            exit()
        elif self.row1[4] == 'x' and self.row2[2] == 'x' and self.row3[0] == 'x':
            print(f'{self.player1} wins!')
            exit()
        else:
            ttt.player1_turn()

    
    def startup(self):
        print('Welcome to Tic Tac Toe!')
        print('1. Player vs Player')
        print('2. Player vs AI')

        self.choice = int(input('Enter your choice: '))

        if self.choice == 1:
            self.player1 = input('Enter player1 name: ')
            ttt.game_start()
        elif self.choice == 2:
            self.player1 = input('Enter player1 name: ')
            print('Enter the number you want to play in.')
            print('1|2|3')
            print('4|5|6')
            print('7|8|9')
            ttt.player1_turn()
        else:
            print('Invalid choice')
            ttt.startup()
            

    
    def game_start(self):
        self.player2 = input('Enter player2 name: ')
        begin = random.randint(1,2)
        print('Enter the number you want to play in.')
        print('1|2|3')
        print('4|5|6')
        print('7|8|9')
        if begin == 1:
            ttt.player1_turn()
        else:
            ttt.player2_turn()

    


ttt = Tik_Tak_Toe()
ttt.startup()