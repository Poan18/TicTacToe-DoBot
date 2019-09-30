import DobotDllType as ddType
from DobotMovement import DobotMovement
from Game import Game
from DobotAi import DobotAi

def start():
    # api = dType.load()
    # state = state = dType.ConnectDobot(api, "", 115200)[0]
    # print("Connect status:",CON_STR[state])
    #
    # if (state != dType.DobotConnect.DobotConnect_NoError):
    #     exit()
    #
    # dh = DobotHandler(dType, api)


    print("Ready to play Tic-Tac-Toe with DoBot?")
    x = 0
    while x == 0:
        pShape = input("""
Who would you like to play as, X or O?
I want to play as: """)
        if pShape.lower() == "x":
            game = Game("X", "O")
            x = 1
        elif pShape.lower() == "o":
            game = Game("O", "X")
            x = 1
        else:
            input("Incorrect input, please check your spelling...")

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

    game.boardStatus()

    while True:
        if game.player == game.turn:
            print("It's your turn!")
            placed = input("Enter your placement " + game.turn + ": ")
            validPlace = game.place(placed)
        else:
            print("DoBots turn\n")
            move = ai.decideMove()
            validPlace = game.place(move)
        if validPlace:
            game.boardStatus()
            game.checkWinner()
            game.nextTurn()


if __name__ == "__main__":
    start()
