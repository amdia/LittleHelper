import numpy as np

# Action of the car
FORWARD = 0
BACKWARD = 1
STOP = 2
TURN_LEFT = 3
TURN_RIGHT = 4
#camera
BAND_THRESHOLD = 190


# Sleep for the thread
SLEEP_PRELOADEDPATH_THREAD = 0.01
SLEEP_STMCONTROLLER_THREAD = 0.01
SLEEP_CHECKDISTANCE_THREAD = 0.01
SLEEP_DETECTOBSTACLE_THREAD = 0.01
SLEEP_CAMERA_THREAD = 0.01

# Semaphore

BLOCKING = True
NON_BLOCKING = False

# color thresholds
LOWER_GRAY = np.array([0, 0, 0])
UPPER_GRAY = np.array([200, 50, 200])

LOWER_BLUE = np.array([100, 20, 0])
UPPER_BLUE = np.array([120, 255, 250])
