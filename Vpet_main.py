# Button serving script: runs repeatedly
from datetime import datetime
import time
import sys
import RPi.GPIO as GPIO


# Sound trigger library content
from gpiozero import OutputDevice
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Neopixel libraries
from neopixel import *

# LED strip configuration:
LED_COUNT = 17 # Number of LED pixels.
LED_PIN = 18 # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 # DMA channel to use for generating signal (try 5)
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)


# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)

# Strip LED Settings
smileLED = {
    'neoNumbers' : [2,3,4,5,6,7,8,9,10,11,12,13,14],
    'color' : {'g': 235,'r': 16, 'b' : 0}
}

neutralLED = {
    'neoNumbers' : [2,3,4,7,8,9,10,11,12,13,14],
    'color' : {'g': 235,'r': 235, 'b' : 0}
    
}
sadLED = {
    'neoNumbers' : [0,1,2,3,4,7,8,11,12,15,16],
    'color' : {'g': 150,'r': 235, 'b' : 0}
}

angryLED = {
    'neoNumbers' : [0,1,2,3,4,5,6,7,8,10,11,12,13,15,16],
    'color' : {'g': 16,'r': 235, 'b' : 0}
}
# Intialize the library (must be called once before other functions).
strip.begin()


# Start by reading the existing JSON file, if it exists.
IDLE_DAYTIME = 1
Smile = 2
Neutral = 3
Sad = 4
Angry = 5
BUTTON_DONE = 6

state = Smile #IDLE_DAYTIME

jsonLastWrittenTime = datetime.now()

def readJSON():
    pass

def writeJSON():
    print("writeJSON")


def sampleButton():
    print("SAMPLE")
    
    
    input_state = GPIO.input(9)
    if input_state == False:
        return 1
    else:
        return 0

def middleOfDay():
    now = datetime.now()
    hour = now.hour
    return hour > 12 and hour < 13
    strip.begin()

def stateForTime():
    # Return IDLE, Smile, Neutral, Sad, Angry LED smiley, depending on time of day:
    now = datetime.now()
    hour = now.hour

    if hour >= 20:
        return Smile
        
        # Sound "hello"
        out= OutputDevice(26 ,False)
        out.on()
        sleep(0.126)
        out.toggle()
        
        # Run Neopixel "smileLED", green
        strip.begin()
        for i in smileLED['neoNumbers']:
            strip.setPixelColorRGB(i, smileLED['color']['g'], smileLED['color']['r'], smileLED['color']['b'])
            strip.show()
        
    elif hour >= 21:
        return Neutral
    
        # Sound "Snore"
        strip.begin()
        out= OutputDevice(19 ,False)
        out.on()
        sleep(0.126)
        out.toggle()
        
         # Run Neopixel "neutralLED", green
        strip.begin()
        for i in neutralLED['neoNumbers']:
            strip.setPixelColorRGB(i, neutralLED['color']['g'], neutralLED['color']['r'], neutralLED['color']['b'])
            strip.show()
        
    elif hour >= 22:
        return Sad
    
        # Sound "Whine"
        out= OutputDevice(13 ,False)
        out.on()
        sleep(0.126)
        out.toggle()
        
         # Run Neopixel "sadLED", green
        strip.begin()
        for i in sadLED['neoNumbers']:
            strip.setPixelColorRGB(i, sadLED['color']['g'], sadLED['color']['r'], sadLED['color']['b'])
            strip.show()
        
    elif hour >= 23:
        return Angry
    
        # Sound "Grunt"
        out= OutputDevice(6 ,False)
        out.on()
        sleep(0.126)
        out.toggle()
        
         # Run Neopixel "angryLED", green
        strip.begin()
        for i in angryLED['neoNumbers']:
            strip.setPixelColorRGB(i, angryLED['color']['g'], angryLED['color']['r'], angryLED['color']['b'])
            strip.show()
        
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
