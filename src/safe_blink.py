#! /usr/bin/python3
# specify the python interpreter

import RPi.GPIO as GPIO
from time import sleep
from signal import signal, SIGTERM, SIGHUP

led_pin = 21 # use a variable for the pin number

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)    # Use Broadcom (processor) pin numbering
# Set pin to be an output pin and set initial value to low (off)
GPIO.setup(led_pin,GPIO.OUT,initial=GPIO.LOW)

def safe_exit(signum, frame):
    exit()

try:
    signal(SIGTERM, safe_exit) # handle pkill
    signal(SIGHUP, safe_exit)  # handle parent close
        
    while True: # Run forever
        GPIO.output(led_pin, GPIO.HIGH) # Turn on
        sleep(2)                        # Sleep for 2 seconds
        GPIO.output(led_pin, GPIO.LOW)  # Turn off
        sleep(1)                        # Sleep for 1 second

# Prevent Traceback warning when using Ctrl-C to exit the program
except KeyboardInterrupt:
    pass

# Cleanup if program closes due to a signal
finally:
    GPIO.cleanup()
