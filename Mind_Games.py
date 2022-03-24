from gpiozero import LED, Button
from time import sleep
import random


class Settings():
    num_io = 2
    gameover = False
    time = 0.1
    generate_sequencecheck = 0
    sequence_ledlength = 0
    sequence_showcheck = 1
    show_sequence = 1
    input_check = 0
    led_length = 5
    led1 = LED(17)
    led2 = LED(27)
#    led3 = LED(22)
#    led4 = LED(23)
#    led5 = LED(24)


class Game():
    def __init__(self):
        self.button1 = Button(25, pull_up=False)
        self.button2 = Button(5, pull_up=False)
#        button3 = Button(6, pull_up=False)
#        button4 = Button(16, pull_up=False)
#        button5 = Button(26, pull_up=False)
        self.sequence = Sequence()
        self.button1.when_pressed = self.sequence.input1
        self.button2.when_pressed = self.sequence.input2
        run = False
    def run(self):
        self.run = True
        while self.run:
            self.sequence.generate_sequence()
            self.sequence.show_sequence(Settings.time)
            self.sequence.wait_for_input()

class Sequence():
    def __init__(self):
        self.sequence = []
        self.input_enabled = False
        self.input_position = 0

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


    def input1(self):
        Settings.led1.on()
        sleep(0.2)
        Settings.led1.off()
        self.check_sequence(1)

    def input2(self):
        Settings.led2.on()
        sleep(0.2)
        Settings.led2.off()
        self.check_sequence(2)

    def check_sequence(self, button_id):
        self.input_position += 1
        if self.sequence[self.input_position - 1] == button_id:
            print("Gut")
        else:
            print("Falsch")
        print(Settings.led_length)
        if self.input_position == Settings.led_length:
            self.input_enabled = False
            self.sequence = []

    def wait_for_input(self):
        self.input_position = 0
        self.input_enabled = True
        while self.input_enabled:
            sleep(0.1)


game = Game()
game.run()
