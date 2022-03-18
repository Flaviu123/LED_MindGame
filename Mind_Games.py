import gpiozero
import time
import random

print("Drücke einen Knopf um das Spiel zu beginnen")
button.when_pressed = Game.

class Settings():
    LED1 = LED(17)
    LED2 = LED(27)
    LED3 = LED(22)
    LED4 = LED(23)
    LED5 = LED(24)
    level_ind = 0
    led_count_lvl = 3
    led_choose = 0

    Button1 = Button(25, pull up = False)
    Button2 = Button(5, pull up = False)
    Button3 = Button(6, pull up = False)
    Button4 = Button(16, pull up = False)
    Button5 = Button(26, pull up = False)

class Game():

    def newlvl(self):
        while Settings.led_choose <= Settings.led_count_lvl:
