from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# Change localhost to Raspberry Pi host and run
# this program on a remote computer
factory = PiGPIOFactory(host='localhost')
led = LED(21, pin_factory=factory)

try:
    # toggle the led forever
    while True:
        led.on()
        sleep(2)
        led.off()
        sleep(2)
    
# Prevent Traceback warning when using Ctrl-C to exit the program
except KeyboardInterrupt:
    pass

# Cleanup if program closes due to a signal
finally:
    led.close()  # close the conntection to the pin
