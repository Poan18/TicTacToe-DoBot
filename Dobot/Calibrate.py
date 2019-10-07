from DobotMovement import DobotMovement
""" Calibrates DoBot and board. Run before starting game """

def startCalibrate():
    dm = DobotMovement()

    print("Setting home location")
    dm.calibrate(1)
    input("Press enter when DoBot stops moving...")

    print(
    """
Please place the middle-right square in the playfield under the suction cup.

- - -
- - X
- - -
    """)

    dm.calibrate(2)
    input("Press enter when done...")
    print(
    """
Please place the middle-right square in the playfield under the suction cup

- - -
X - -
- - -
    """)

    dm.calibrate(3)
    input("Press enter when done...")
    print("You may now start the game with 'python start.py'")


if __name__ == "__main__":
    startCalibrate()
