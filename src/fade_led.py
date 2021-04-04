from signal import pause
from gpiozero import PWMLED

light = PWMLED(21) # create a PWMLED object called "led"

try:
    light.pulse()  # blink the LED with fade-in and fade-out time
    pause()        # pause the program

except KeyboardInterrupt:  # capture CTRL-C to prevent warning
    pass

finally:
    light.close()  # clean up the GPIO