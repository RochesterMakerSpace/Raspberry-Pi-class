import RPi.GPIO as IO            # helps us use GPIO’s of PI
import time                      # time to provide delays in program
IO.setwarnings(False)            # do not show any warnings
IO.setmode (IO.BCM)              # programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
IO.setup(19,IO.OUT)              # initialize GPIO19 as an output
p = IO.PWM(19,100)               # GPIO19 as PWM output, with 100Hz frequency
p.start(0)                       # generate PWM signal with 0% duty cycle
while True:                      # loop forever
    for x in range (50):         # variable x incremented from 0-49
        p.ChangeDutyCycle(x)     # change duty cycle to vary the brightness of LED.
        time.sleep(0.1)          # sleep for 100ms
		
    for x in range (50):         # variable x incremented from 0 to 49.
        p.ChangeDutyCycle(50-x)  # change duty cycle to vary the brightness of LED.
        time.sleep(0.1)          # sleep for 100ms
