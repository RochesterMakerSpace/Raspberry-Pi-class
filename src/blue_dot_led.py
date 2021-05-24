from bluedot import BlueDot
from gpiozero import LED

bd = BlueDot()
led = LED(21)

try:
    while True:
        bd.wait_for_press()
        led.on()
        bd.wait_for_release()
        led.off()
        
# Prevent Traceback warning when using Ctrl-C to exit the program
except KeyboardInterrupt:
    pass # no-op

finally:
    led.close()
    bd.stop()


    