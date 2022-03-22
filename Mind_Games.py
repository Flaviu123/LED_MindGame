import gpiozero
import time
import random

print("Drücke einen Knopf um das Spiel zu beginnen")
button.when_pressed = Game.


class Settings():
    num_io = 2
    LED1 = LED(17)
    LED2 = LED(27)
    LED3 = LED(22)
    LED4 = LED(23)
    LED5 = LED(24)

    Button1 = Button(25, pull
    up = False)
    Button2 = Button(5, pull
    up = False)
    Button3 = Button(6, pull
    up = False)
    Button4 = Button(16, pull
    up = False)
    Button5 = Button(26, pull
    up = False)

    class Game():

    class Level():
        def __init__(self):
            self.level_ind = 0
            self.led_lenght = 2
            self.time = 2

        def next_level(self):
            pass

        def reset_level(self):
            pass

    class Sequence():
        def __init(self):
            sequence = []
            led_choose = (1, Settings.num_io)

        def generate_sequence(led_lenght, time):
            random.uniform(led_choose)
            pass

        def show_sequence():
            pass

        def user_sequnce():
            pass

        def check_sequnce():
            return

    start.game()