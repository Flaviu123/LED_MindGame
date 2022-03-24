from gpiozero import LED, Button
from time import sleep
import random


class Settings():
    num_io = 2
    gameover = False
    time = 2
    generate_sequencecheck = 0
    sequence_ledlength = 0
    sequence_showcheck = 1
    show_sequence = 1
    input_check = 0
    led_length = 5
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



class Sequence():
    def __init__(self):
        self.sequence = []
        self.playerinputlist = []

    def generate_sequence(self):
        for i in range(0, Settings.led_length):
            add_s = random.uniform(1, Settings.num_io)
            self.sequence.append(add_s)
            Settings.generate_sequencecheck += 1
            if Settings.generate_sequencecheck == Settings.led_length:
               self.show_sequence(Settings.time)


    def show_sequence(self, time):
        for i in range(0, Settings.led_length + 1):
            if self.sequence[Settings.show_sequence - 1] == 1:
                LED1.on()
                Settings.show_sequence += 1
                sleep(time)
                LED1.off()

            elif self.sequence[Settings.show_sequence - 1] == 2:
                LED2.on()
                Settings.show_sequence += 1
                sleep(time)
                LED2.off()

            elif self.sequence[Settings.show_sequence - 1] == 3:
                LED3.on()
                Settings.show_sequence += 1
                sleep(time)
                LED3.off()

            elif self.sequence[Settings.show_sequence - 1] == 4:
                LED4.on()
                Settings.show_sequence += 1
                sleep(time)
                LED4.off()

            elif self.sequence[Settings.show_sequence - 1] == 5:
                LED5.on()
                Settings.show_sequence += 1
                sleep(time)
                LED5.off()

            elif len(self.sequence) == Settings.show_sequence - 1:
                Settings.show_sequence = 1
                self.input_sequence()


    def player_input(self):
        if Settings.Button1.is_pressed:
            self.playerinputlist.append(1)
            self.check_sequence()

        elif Settings.Button2.is_pressed:
            self.playerinputlist.append(2)
            self.check_sequence()

        elif Settings.Button3.is_pressed:
            self.playerinputlist.append(3)
            self.check_sequence()

        elif Settings.Button4.is_pressed:
            self.playerinputlist.append(4)
            self.check_sequence()

        elif Settings.Button5.is_pressed:
            self.playerinputlist.append(5)
            self.check_sequence()

        elif len(self.playerinputlist) == len(self.sequence):
            pass #Whileschleife wird unterbrochen



    def check_sequence(self):
        if self.sequence[Settings.input_check] == self.playerinputlist[Settings.input_check]:
            print("Richtige LED gemerkt!")
            Settings.input_check += 1
        else:
            pass #GAME RESTART
