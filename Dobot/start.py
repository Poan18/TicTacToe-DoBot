import DobotDllType as ddType
from DobotMovement import DobotMovement
from Game import Game
from DobotAi import DobotAi
import os
""" File that starts the game """

def start():
    """ Function which starts the game """
    os.system("cls")
    print("Ready to play Tic-Tac-Toe with DoBot?")

    """ Select which shape player wants to be """
    x = 0
    while x == 0:
        pShape = input("""
Who would you like to play as, X or O?
--> """)
        if pShape.lower() == "x":
            game = Game("X", "O")
            x = 1
        elif pShape.lower() == "o":
            game = Game("O", "X")
            x = 1
        else:
            print(chr(27) + "[2J" + chr(1) + "[;H")
            input("Incorrect input, please check your spelling...")

    """ Select who goes first """
    x = 0
    while x == 0:
        fTurn = input("""
Who should go first?
1) Player
2) DoBot """)
        if fTurn.lower() == "1":
            game.setFirstTurn("1")
            x = 1
        elif fTurn.lower() == "2":
            game.setFirstTurn("2")
            x = 1
        else:
            input("Incorrect input, please check your spelling...")

    ai = DobotAi(game, DobotMovement(), "easy")

    # ai = DobotAi(game, "easy")

    print("Good luck and have fun!")
    input("\nPress enter to continue...")
    os.system("cls")
    print("Board status")
    game.boardStatus()

    """ While loop that runs until game.announceWinner() finds winner """
    while True:
        if game.player == game.turn:
            """ Player turn """
            print("It's your turn!")
            placed = input("Enter your placement " + game.turn + ": ")
            validPlace = game.place(placed)
            os.system("cls")
        else:
            """ DoBot Turn """
            print("DoBots turn\n")
            move = ai.decideMove()
            validPlace = game.place(move)
        if validPlace:
            """ If valid placement, show board, check if they won or proceed to next turn """
            print("Board status")
            game.boardStatus()
            game.checkWinner()
            game.nextTurn()
        else:
            """ If not valid placement, show board and message """
            game.boardStatus()
            print("Invalid placement, enter a free position between 0-8\n")


if __name__ == "__main__":
    start()
