from gpiozero import LED
from threading import Timer
from signal import pause
import sys

light = LED(21) # create a light object using GPIO21

def blink():
    light.toggle()      # toggle the light
    t = Timer(1,blink)  # create a timer with 1 second timeout, call hello on timeout
    t.start()           # start the timer

try:
    blink() # excecute function hello()

    pause() # pause and wait for keyboard input
    
# Prevent Traceback warning when using Ctrl-C to exit the program
except KeyboardInterrupt:
    pass

finally:
    light.close()  # close the conntection to the pin
    sys.exit()     # will stop the timer when exiting the program
  