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
        """ Calculated where to place his piece """

        while True:
            rngPlace = random.randint(0, 8)
            if self.currGame.board[int(rngPlace)] == "_":
                self.dm.placePos(rngPlace)
                time.sleep(3)
                return rngPlace
