from time import sleep
from gpiozero import PWMLED
from math import log10

light = PWMLED(21)

loop_delay = 0.2  # delay in seconds between each brightness change

# three brightness change algorithms
algorithms = ["linear", "power_2", "logarithmic"]
algorithm = algorithms[0]

steps = 10     # number of brigntness steps
fade_factor = (steps * log10(2))/(log10(steps))

led_min = 0          # minimum led brightness
led_max = 100         # maximum led brightness
led_step = 100/steps # brightness change

def brightness(level):
    if algorithm == "power_2":
        return pow(2, level/10)/1024
    elif algorithm == "logarithmic":
        return (pow(2, ((level/led_step)/fade_factor))-1)/steps
    else:
        # default to linear
        return level/100

            

try:
    while True:                       # loop forever
        for level in range (led_min,led_max+1,int(led_step)):  # variable x incremented from min to max by step
            bright = brightness(level) # calculate new duty cycle
            print("increasing:", level, bright*100) # print for debug
            light.value = bright       # change duty cycle to vary the brightness of LED.
            sleep(loop_delay)          # sleep in seconds
            
        for level in range (led_max,led_min-1,int(-led_step)): # variable x decremented from max to min by step
            bright = brightness(level) # calculate new duty cycle
            print("decreasing:", level, bright*100) # print for debug
            light.value = bright       # change duty cycle to vary the brightness of LED.
            sleep(loop_delay)          # sleep in seconds

except KeyboardInterrupt:
    pass

finally:
    light.close()