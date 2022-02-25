import gpiozero
import time

class Settings():
    LED1 = LED(17)
    LED2 = LED(27)
    LED3 = LED(22)
    LED4 = LED(23)
    LED5 = LED(24)

    Button1 = Button(25, pull up = False)
    Button2 = Button(5, pull up = False)
    Button3 = Button(6, pull up = False)
    Button4 = Button(16, pull up = False)
    Button5 = Button(26, pull up = False)

class Button():
    def __init__(self):
	pass
