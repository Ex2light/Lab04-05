import os
from random import randint

class TicTacToe:
    def __init__(self) -> object:
        self.board = [['*', '*', '*'] for x in range(3)]
        self.End = False
        self.xWin = False
        self.moveCounter = 0

    def printBoard(self):
        for i in self.board:
            print(i[0] + ' ' + i[1] + ' ' + i[2])

    def sendBoard(self):
        self.toSend = ""
        for i in self.board:
            print(i[0] + ' ' + i[1] + ' ' + i[2])
            self.toSend += i[0]
            self.toSend += i[1]
            self.toSend += i[2]
        return self.toSend

    def movePlayer1(self,move):
        index = move
        if index > 9:
            print("Spot out of range, select other")
            self.movePlayer1()

        elif self.board[(index - 1) // 3][(index % 3) - 1] == '*':
            self.board[(index - 1) // 3][(index % 3) - 1] = 'X'
            self.moveCounter += 1
        else:
            if self.board[(index - 1) // 3][(index % 3) - 1] == 'X':
                print("Spot ocupied by You, select other")
                self.movePlayer1()
            elif self.board[(index - 1) // 3][(index % 3) - 1] == 'O':
                print("Spot ocupied by Computer, select other")
                self.movePlayer1()


        self.isEnd()

    def movePlayer2(self):
        index = randint(1,9)

        if self.board[(index - 1) // 3][(index % 3) - 1] == '*':
            self.board[(index - 1) // 3][(index % 3) - 1] = 'O'
            self.moveCounter += 1

        else:
            if self.board[(index - 1) // 3][(index % 3) - 1] == 'X':
                self.movePlayer2()
            elif self.board[(index - 1) // 3][(index % 3) - 1] == 'O':
                self.movePlayer2()

            
        self.isEnd()

    def game(self):
        print("Welcome to the tic-tac-toe game.\nFirst player is 'X' , Computer is 'O'.\nTo enter your moves type numbers 1-9")
        self.printBoard()
        while not self.End:
            self.movePlayer1()
            #os.system("clear")
            self.printBoard()
            if not self.End:
                if self.moveCounter == 9:
                    break
                print("Computer turn")
                self.movePlayer2()
                #os.system("clear")
                self.printBoard()
        if self.xWin:
            print("Player 1 has won")
        elif self.End:
            print("Computer has won :(")
        else:
            print("Draw")

    def isEnd(self):
        for i in range(3):
            if self.board[i] == ['X', 'X', 'X']:
                self.xWin = True
                self.End = True
            if self.board[i] == ['O', 'O', 'O']:
                self.End = True
            for j in range(3):
                if self.board[j][i] != 'X':
                    break
            else:
                self.xWin = True
                self.End = True

            for j in range(3):
                if self.board[j][i] != 'O':
                    break
            else:
                self.End = True
        for k in range(3):
            if self.board[k][k] != 'X':
                break
        else:
            self.End = True
            self.xWin = True
        for k in range(3):
            if self.board[k][k] != 'O':
                break
        else:
            self.End = True

        if self.board[1][1] == self.board[0][2] == self.board[2][0] != '*':
            self.End = True
            if self.board[1][1] == 'X':
                self.xWin = True
