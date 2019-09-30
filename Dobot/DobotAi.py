import random
import time
from DobotMovement import DobotMovement
""" Module with DobotAi class """


class DobotAi():
    """ DobotAi decisions """

    def __init__(self, game, dm=None, difficulty="easy"):
        self.diff = difficulty
        self.currGame = game
        self.dm = dm

    def decideMove(self):
        while True:
            rngPlace = random.randint(0, 8)
            if self.currGame.board[int(rngPlace)] == "_":
                print("Before place")
                print(rngPlace)
                self.dm.placePos(rngPlace)
                print("After place")
                time.sleep(3)
                return rngPlace
