import sys
import threading
import Dobot.DobotDllType as dType
from Dobot.test import testy

""" Module with Dobot class """

class DobotHandler():
    """ Handles DoBot actions """

    def __init__(self):
        self.api = dType.load()
        pass

    def pickup(self):
        testy.hello()

    def place(self):
        pass

if __name__ == "__main__":
    DobotHandler().pickup()
