from gpiozero import LED, Button
from time import sleep
import random


class Settings():
    num_io = 2
    gameover = False
    time = 0.5
    generate_sequencecheck = 0
    sequence_ledlength = 0
    sequence_showcheck = 1
    show_sequence = 1
    input_check = 0
    led_length = 5
    led1 = LED(17)
    led2 = LED(27)
    led3 = LED(22)
    led4 = LED(23)
    led5 = LED(24)

    button1 = Button(25, pull_up=False)
    button2 = Button(5, pull_up=False)
    button3 = Button(6, pull_up=False)
    button4 = Button(16, pull_up=False)
    button5 = Button(26, pull_up=False)


class Game():
    def __init__(self):
        run = False
        self.sequence = Sequence()

    def run(self):
        self.run = True
        while self.run:
            self.sequence.generate_sequence()
            self.sequence.show_sequence(Settings.time)



class Sequence():
    def __init__(self):
        self.sequence = []
        self.playerinputlist = []

    def generate_sequence(self):
        for i in range(0, Settings.led_length):
            add_s = random.randint(1, Settings.num_io)
            self.sequence.append(add_s)

    def show_sequence(self, time):
        for i in self.sequence:
            if i == 1:
                print("1")
                Settings.led1.on()
                sleep(time)
                Settings.led1.off()
                sleep(time)

            elif i == 2:
                print("2")
                Settings.led2.on()
                sleep(time)
                Settings.led2.off()
                sleep(time)

            """elif i == 3:
                Settings.led3.on()
                sleep(time)
                Settings.led3.off()
                sleep(time)

            elif i == 4:
                Settings.led4.on()
                sleep(time)
                Settings.led4.off()
                sleep(time)

            elif i == 5:
                Settings.led5.on()
                sleep(time)
                Settings.led5.off()
                sleep(time)"""


        #self.input_sequence()


    def player_input(self):
        if Settings.button1.is_pressed:
            self.playerinputlist.append(1)
            self.check_sequence()

        elif Settings.button2.is_pressed:
            self.playerinputlist.append(2)
            self.check_sequence()

        #elif Settings.button3.is_pressed:
            #self.playerinputlist.append(3)
            #self.check_sequence()

        #elif Settings.button4.is_pressed:
            #self.playerinputlist.append(4)
            #self.check_sequence()

        #elif Settings.button5.is_pressed:
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

game = Game()
game.run()
