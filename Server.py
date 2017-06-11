from TicTacToe import *
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

print("Waiting for connection ")
while True:
    print(". ")
    connection, client_address = sock.accept()
    if connection or client_address:
        break

try:
    print("Connection from: " + str(client_address))

    while True:
        connection.sendall(str.encode("1. Tic-Tac-Toe\n2. Guess number\n3. Close"))
        data = connection.recv(1024)
        which_option = data.decode()
        which_option = int(which_option)
        if which_option == 1:
            Game = TicTacToe()

            connection.sendall(str.encode("Welcome to the tic-tac-toe game.\nFirst player is 'X' , Computer is 'O'.\nTo enter your moves type numbers 1-9"))
            Game.printBoard()
            board = Game.sendBoard()
            connection.sendall(str.encode(board))
            while not Game.End:
                connection.sendall(str.encode("Player 1 turn. Type next position"))
                Game.movePlayer1()
                Game.printBoard()
                board = Game.sendBoard()
                connection.sendall(str.encode(board))
                move = int(data.decode())
                Game.movePlayer1(move)
                if not Game.End:
                    if Game.moveCounter == 9:
                        break
                    connection.sendall(str.encode("Computer turn"))
                    Game.movePlayer2()
                    Game.printBoard()
                    board = Game.sendBoard()
                    connection.sendall(str.encode(board))
            if Game.xWin:
                connection.sendall(str.encode("Player 1 has won"))
            elif Game.End:
                connection.sendall(str.encode("Computer has won :("))
            else:
                connection.sendall(str.encode("Draw"))

        if which_option==2:
            numberToGuess=random.randint(0, 100)
            attempts=0
            connection.sendall(str.encode("Guess number!"))
            while True:
                data = connection.recv(1024)
                playersAnswer=int(data.decode())
                if(playersAnswer==numberToGuess):
                    connection.sendall(str.encode("Correct. Number of attempts is ".format(attempts)))
                    break
                if(playersAnswer<numberToGuess):
                    connection.sendall(str.encode("Your number is too low"))
                    attempts+=1
                if(playersAnswer>numberToGuess):
                    connection.sendall(str.encode("Your number is too high"))
                    attempts += 1
        if which_option==3:
            print("End")
            connection.close()


except:
    connection.sendall("Error during connection")

finally:
    print("Closing connection.")
    connection.close()

