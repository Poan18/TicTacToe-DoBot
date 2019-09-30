import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "Dobot is connected without Errors",
    dType.DobotConnect.DobotConnect_NotFound: "Dobot can't be found",
    dType.DobotConnect.DobotConnect_Occupied: "Dobot is occupied"}

""" Module with Dobot class """

class DobotMovement():
    """ Handles DoBot movement """

    def __init__(self):
        self.api = dType.load()
        self.pieces = 5
        state = dType.ConnectDobot(self.api, "", 115200)[0]
        print("Connect status:",CON_STR[state])
        if state != dType.DobotConnect.DobotConnect_NoError:
            exit()
        dType.SetHOMEParams(self.api, 250, 0, 50, 0, isQueued = 1)
        dType.SetPTPJointParams(self.api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
        dType.SetPTPCommonParams(self.api, 100, 100, isQueued = 1)

    def home(self):
        dType.SetQueuedCmdClear(self.api)

        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, 0, 50, 0, isQueued = 1)

        #Async Home
        dType.SetHOMECmd(self.api, temp = 0, isQueued = 1)
        dType.SetQueuedCmdStartExec(self.api)
        dType.DisconnectDobot(self.api)

    def hover(self):
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, 0, 50, 0)

    def suck(self):
        dType.SetQueuedCmdClear(self.api)

        dType.SetEndEffectorSuctionCup(self.api, 1, 1)
        dType.SetWAITCmd(self.api, 1, 1)
        dType.SetEndEffectorSuctionCup(self.api, 0, 1)

        dType.SetQueuedCmdStartExec(self.api)

    def testQ(self):
        dType.SetQueuedCmdClear(self.api)
        r = 0

        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 300, 50, -55, r, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 300, 0, -55, r, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 300, -50, -55, r, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, 50, -55, r, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, 0, -55, r, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -55, r, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 200, 50, -55, r, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, -55, r, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 200, -50, -55, r, 1)

        dType.SetQueuedCmdStartExec(self.api)

        dType.DisconnectDobot(self.api)

    def placePos(self, spot):
        print("PlacePos")
        if spot == 0:
            self.placeIt(300, 50, -55)
        elif spot == 1:
            self.placeIt(300, 0, -55)
        elif spot == 2:
            self.placeIt(300, -50, -55)
        elif spot == 3:
            self.placeIt(250, 50, -55)
        elif spot == 4:
            self.placeIt(250, 0, -55)
        elif spot == 5:
            self.placeIt(250, -50, -55)
        elif spot == 6:
            self.placeIt(200, 50, -55)
        elif spot == 7:
            self.placeIt(200, 0, -55)
        elif spot == 8:
            self.placeIt(200, -50, -55)

    def placeIt(self, x, y, z, r=-40):
        dType.SetQueuedCmdClear(self.api)

        self.pick()

        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, x, y, z, r, isQueued = 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, x, y, -65, r, isQueued = 1)
        dType.SetWAITCmd(self.api, 0.5, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, x, y, z, r, isQueued = 1)

        self.hover()

        dType.SetQueuedCmdStartExec(self.api)

    def pick(self):
        stackHeight = (self.pieces*3)+69
        r = -40

        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -40, r)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, stackHeight, r, isQueued = 1)
        dType.SetEndEffectorSuctionCup(self.api, 1, 1)
        dType.SetWAITCmd(self.api, 0.5, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -40, r, isQueued = 1)

    def pickUp(self):
        dType.SetQueuedCmdClear(self.api)

        r = -40
        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -55, r)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -65, r, isQueued = 1)
        dType.SetEndEffectorSuctionCup(self.api, 1, 1)
        dType.SetWAITCmd(self.api, 0.5, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -55, r, isQueued = 1)

        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 300, 50, -55, r, isQueued = 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 300, 50, -65, r, isQueued = 1)
        dType.SetEndEffectorSuctionCup(self.api, 0, 1)
        dType.SetWAITCmd(self.api, 0.5, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 300, 50, -55, r, isQueued = 1)

        dType.SetQueuedCmdStartExec(self.api)

    def maxStack(self):
        dType.SetQueuedCmdClear(self.api)

        stackHeight = (self.pieces*3)+69

        r = -40
        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -40, r)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, stackHeight, r, isQueued = 1)
        dType.SetEndEffectorSuctionCup(self.api, 1, 1)
        dType.SetWAITCmd(self.api, 0.5, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -40, r, isQueued = 1)

        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 300, -50, -40, r, isQueued = 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 300, -50, -65, r, isQueued = 1)
        dType.SetEndEffectorSuctionCup(self.api, 0, 1)
        dType.SetWAITCmd(self.api, 0.5, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 300, -50, -40, r, isQueued = 1)

        dType.SetQueuedCmdStartExec(self.api)
        self.pieces = self.pieces - 1

if __name__ == "__main__":
    dm = ""
    while True:
        if not dm:
            dm = DobotMovement()

        inp = input("""
        slot) 0-8
        testq) Line up all squres
        home) Home
        """)
        if inp == "0":
            dm.place_0()
        elif inp.lower() == "stack":
            dm.maxStack()
        elif inp.lower() == "home":
            dm.home()
        elif inp.lower() == "suck":
            dm.suck()
        elif inp.lower() == "testq":
            dm.testQ()
        elif inp.lower() == "slot":
            while True:
                sl = input("Enter slot: ")
                if sl == "q":
                    break
                elif sl == "p":
                    dm.pickUp()
                else:
                    dm.placePos(int(sl))
