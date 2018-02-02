# Button serving script: runs repeatedly

from datetime import datetime
import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Start by reading the existing JSON file, if it exists.


IDLE_DAYTIME = 1
GREEN = 2
RED = 3
BUTTON_DONE = 4

state = GREEN #IDLE_DAYTIME

jsonLastWrittenTime = datetime.now()

def readJSON():
    pass

def writeJSON():
    print("writeJSON")


def sampleButton():
    print("SAMPLE")
    
    
    input_state = GPIO.input(19)
    if input_state == False:
        return 1
    else:
        return 0

def stateForTine():
    # Return IDLE, GREEN or RED depending on time of day:
    pass

def middleOfDay():
    now = datetime.now()
    hour = now.hour
    return hour > 12 and hour < 13

def stateForTime():
    now = datetime.now()
    hour = now.hour

    if hour < 2:
        return RED
    elif hour >= 15: #20:
        return GREEN
    else:
        return IDLE_DAYTIME

while True:
    # Reset state ready for button etc. if it's the middle of the day:
    if state == BUTTON_DONE and middleOfDay():
        state = IDLE_DAYTIME

    # Progress into the correct colour state:
    if state != BUTTON_DONE:
        state = stateForTime()

    buttonState = sampleButton()

    if buttonState and state != IDLE_DAYTIME:
        state = BUTTON_DONE

    now = datetime.now()
    deltaSecs = (now - jsonLastWrittenTime).total_seconds()

    if deltaSecs > 15:
        writeJSON()
        jsonLastWrittenTime = now

    time.sleep(0.1)
    
    print state
    
    #flush the surpervisor to show log
    sys.stdout.flush()
