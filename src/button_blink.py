from gpiozero import LED, Button
from time import sleep

led_pin = 21     # use a variable for the led pin number
button_pin = 26  # use a variable for the button pin number

led = LED(led_pin)
button = Button(button_pin)

button.wait_for_press()
print('You pushed me')
led.on()
sleep(3)
led.off()
led.close()
