
""" Module with game class """

class Game():
    """ Game logic actions """

    def __init__(self, pPiece, dPiece):
        self.player = pPiece
        self.dobot = dPiece
        self.turn = self.player
        self.board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

    def check(self):
        """ Testing function """
        print(self.board)
        print("Player is playing as: " + self.player)
        print("DoBot is playing as: " + self.dobot)

    def setFirstTurn(self, firstTurn):
        if firstTurn == "1":
            self.turn = self.player
        elif firstTurn == "2":
            self.turn = self.dobot

    def nextTurn(self):
        """ Turn hands over the other person """
        if self.turn == self.player:
            self.turn = self.dobot
        else:
            self.turn = self.player

    def boardStatus(self):
        """ Print status of board """
        for x in range(0, 9, 3):
                print(self.board[x], self.board[x+1], self.board[x+2])
        print("\n")

    def place(self, placed):
        """ Place a piece on the board """
        try:
            if int(placed) > 8 or int(placed) < 0:
                print("Input is not in range")
                return False

            if self.board[int(placed)] == "_":
                self.board[int(placed)] = self.turn
                return True
            else:
                if self.turn == self.player:
                    print("That spot is already taken, try again.")
                return False
        except ValueError:
            print("Invalid input, please try again")
            return False

    def checkWinner(self):
        """ Check if there is a winner or a tie """

        self.checkPattern(0, 1, 2)
        self.checkPattern(3, 4, 5)
        self.checkPattern(6, 7, 8)
        self.checkPattern(0, 3, 6)
        self.checkPattern(1, 4, 7)
        self.checkPattern(2, 5, 8)
        self.checkPattern(0, 4, 8)
        self.checkPattern(2, 4, 6)

        #Tie if no empty spaces left
        if "_" not in self.board:
            print("IT'S A TIE!!")
            exit()

    def checkPattern(self, a, b, c):
        """ Check if there's a winner pattern """
        if self.board[a] == self.turn and self.board[b] == self.turn and self.board[c] == self.turn:
            self.announceWinner()
        else:
            pass


    def announceWinner(self):
        """ Announce the winner and end the game """
        if self.turn == self.player:
            print("PLAYER WINS!!")
        else:
            print("DOBOT WINS!!")

        exit()




if __name__ == "__main__":
    Game()
