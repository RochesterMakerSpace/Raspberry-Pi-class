from signal import pause
from gpiozero import PWMLED

light = PWMLED(21)

try:
    light.pulse(fade_in_time=2, fade_out_time=2)

    pause()

except KeyboardInterrupt:
    pass

finally:
    light.close()