from gpiozero import LED, Button
import time
import random

print("Drücke einen Knopf um das Spiel zu beginnen")


class Settings():
    num_io = 2
    gameover = False
    LED1 = LED(17)
    LED2 = LED(27)
    LED3 = LED(22)
    LED4 = LED(23)
    LED5 = LED(24)

    Button1 = Button(25, pull_up=False)
    Button2 = Button(5, pull_up=False)
    Button3 = Button(6, pull_up=False)
    Button4 = Button(16, pull_up=False)
    Button5 = Button(26, pull_up=False)


class Game():
    run = False

    def __init__(self):
        pass

    def run():
        pass


class Level():
    def __init__(self):
        self.level_ind = 0
        self.led_lenght = 2
        self.time = 0
        self.sequence = None

    def next_level(self):
        pass

    def reset_level(self):
        pass


class Sequence():
    def __init__(self, led_lenght, time):
        self.led_lenght = led_lenght
        self.time = time
        self.sequence = []
        self.user_sequence = []
        self.led_choose = (1, Settings.num_io)

    def generate_sequence(led_lenght, time):
        random.uniform(led_choose)
        pass

    def show_sequence():
        pass

    def user_sequnce():
        pass

    def check_sequnce():
        return
