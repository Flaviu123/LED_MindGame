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
            add_s = random.randint(1, Settings.num_io)
            self.sequence.append(add_s)
        self.show_sequence(Settings.time)


    def show_sequence(self, time):
        for i in self.sequence:
            if i == 1:
                print("1")
                Settings.LED1.on()
                sleep(time)
                Settings.LED1.off()
                sleep(time)

            elif i == 2:
                print("2")
                Settings.LED2.on()
                sleep(time)
                Settings.LED2.off()
                sleep(time)

            """elif i == 3:
                Settings.LED3.on()
                sleep(time)
                Settings.LED3.off()
                sleep(time)

            elif i == 4:
                Settings.LED4.on()
                sleep(time)
                Settings.LED4.off()
                sleep(time)

            elif i == 5:
                Settings.LED5.on()
                sleep(time)
                Settings.LED5.off()
                sleep(time)"""


        self.input_sequence()


    def player_input(self):
        if Settings.Button1.is_pressed:
            self.playerinputlist.append(1)
            self.check_sequence()

        elif Settings.Button2.is_pressed:
            self.playerinputlist.append(2)
            self.check_sequence()

        #elif Settings.Button3.is_pressed:
            #self.playerinputlist.append(3)
            #self.check_sequence()

        #elif Settings.Button4.is_pressed:
            #self.playerinputlist.append(4)
            #self.check_sequence()

        #elif Settings.Button5.is_pressed:
            #self.playerinputlist.append(5)
            #self.check_sequence()

        elif len(self.playerinputlist) == len(self.sequence):
            pass #Whileschleife wird unterbrochen



    def check_sequence(self):
        if self.sequence[Settings.input_check] == self.playerinputlist[Settings.input_check]:
            print("Richtige LED gemerkt!")
            Settings.input_check += 1
        else:
            pass #GAME RESTARTd

s = Sequence()
s.generate_sequence()
