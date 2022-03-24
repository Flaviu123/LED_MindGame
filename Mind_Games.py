from gpiozero import LED, Button
from time import sleep
import random


class Settings():
    num_io = 2
    gameover = False
    sequence_ledlength = 0
    sequence_showcheck = 1
    show_sequence = 1
    input_check = 0
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
        self.led_length = 2
        self.time = 0
        self.sequence = None

    def next_level(self):
        self.sequence = Sequence(self.led_length, self.time)


    def reset_level(self):
        pass


class Sequence():
    def __init__(self, led_length, time):
        self.led_length = led_length
        self.time = time
        self.sequence = []
        self.playerinput = []

    def generate_sequence(self, led_length):
        for i in range(0, led_lenght):
            add_s = random.uniform(1, Settings.num_io)
            self.sequence.append(add_s)


    def show_sequence(self, time):
        if Settings.sequence_showcheck == Settings.show_sequence:
            if self.sequence[Settings.show_sequence - 1] == 1:
                LED1.on()
                sleep(time)
                LED1.off()

            elif self.sequence[Settings.show_sequence - 1] == 2:
                LED2.on()
                sleep(time)
                LED2.off()

            elif self.sequence[Settings.show_sequence - 1] == 3:
                LED3.on()
                sleep(time)
                LED3.off()

            elif self.sequence[Settings.show_sequence - 1] == 4:
                LED4.on()
                sleep(time)
                LED4.off()

            elif self.sequence[Settings.show_sequence - 1] == 5:
                LED5.on()
                sleep(time)
                LED5.off()

        if len(self.sequence) == Settings.sequence_showcheck:
            Settings.show_sequence = 1
            Settings.sequence_showcheck = 1
            self.input_sequence()

        else:
            Settings.show_sequence += 1
            Settings.sequence_showcheck += 1
            self.show_sequence()


    def player_input(self):
        if Settings.Button1.is_pressed:
            self.playerinput.append(1)
            self.check_sequence()

        if Settings.Button2.is_pressed:
            self.playerinput.append(2)
            self.check_sequence()

        if Settings.Button3.is_pressed:
            self.playerinput.append(3)
            self.check_sequence()

        if Settings.Button4.is_pressed:
            self.playerinput.append(4)
            self.check_sequence()

        if Settings.Button5.is_pressed:
            self.playerinput.append(5)
            self.check_sequence()
            
            


    def check_sequence(self):
        if self.sequence[Settings.input_check] == self.playerinput[Settings.input_check]:
            print("Richtige LED gemerkt!")
            Settings.input_check += 1
        else:
            pass #GAME RESTART
