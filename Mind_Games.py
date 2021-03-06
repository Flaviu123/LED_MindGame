from gpiozero import LED, Button
from time import sleep
import random


class Settings():
    num_io = 5
    led1 = LED(17)
    led2 = LED(27)
    led3 = LED(22)
    led4 = LED(23)
    led5 = LED(24)


class Game():
    def __init__(self):
        self.button1 = Button(25, pull_up=False)
        self.button2 = Button(5, pull_up=False)
        self.button3 = Button(6, pull_up=False)
        self.button4 = Button(16, pull_up=False)
        self.button5 = Button(26, pull_up=False)
        self.sequence = Sequence()
        self.button1.when_pressed = self.sequence.input1
        self.button2.when_pressed = self.sequence.input2
        self.button3.when_pressed = self.sequence.input3
        self.button4.when_pressed = self.sequence.input4
        self.button5.when_pressed = self.sequence.input5
        self.running = False
        
    def run(self):
        self.running = True
        while self.running:
            self.sequence.generate_sequence()
            self.sequence.show_sequence()
            self.sequence.wait_for_input()
            

class Sequence():
    def __init__(self):
        self.sequence = []
        self.allow_input = False
        self.input_position = 0
        self.time = 0.5
        self.led_length = 5

    def generate_sequence(self):
        for i in range(0, self.led_length):
            add_s = random.randint(1, Settings.num_io)
            self.sequence.append(add_s)

    def show_sequence(self):
        for i in self.sequence:
            if i == 1:
                Settings.led1.on()
                sleep(self.time)
                Settings.led1.off()
                sleep(self.time)

            elif i == 2:
                Settings.led2.on()
                sleep(self.time)
                Settings.led2.off()
                sleep(self.time)

            elif i == 3:
                Settings.led3.on()
                sleep(self.time)
                Settings.led3.off()
                sleep(self.time)
                
            elif i == 4:
                Settings.led4.on()
                sleep(self.time)
                Settings.led4.off()
                sleep(self.time)
                
            elif i == 5:
                Settings.led5.on()
                sleep(self.time)
                Settings.led5.off()
                sleep(self.time)
                

    def input1(self):
        if self.allow_input == True:
            Settings.led1.on()
            sleep(0.2)
            Settings.led1.off()
            self.check_sequence(1)

    def input2(self):
        if self.allow_input == True:
            Settings.led2.on()
            sleep(0.2)
            Settings.led2.off()
            self.check_sequence(2)
        
    def input3(self):
        if self.allow_input == True:
            Settings.led3.on()
            sleep(0.2)
            Settings.led3.off()
            self.check_sequence(3)
        
    def input4(self):
        if self.allow_input == True:
            Settings.led4.on()
            sleep(0.2)
            Settings.led4.off()
            self.check_sequence(4)
        
    def input5(self):
        if self.allow_input == True:
            Settings.led5.on()
            sleep(0.2)
            Settings.led5.off()
            self.check_sequence(5)

    def check_sequence(self, button_id):
        self.input_position += 1
        if self.sequence[self.input_position - 1] == button_id:
           print(f"Richtig! {self.input_position}/{self.led_length}")
        else:
            print("Gameover!")
            self.reset_level()
        if self.input_position == self.led_length:
            self.increase_difficulty()
            Settings.led3.on()
            print("N??chstes Level beginnt in 3 Sekunden!")
            sleep(1)
            Settings.led2.on()
            Settings.led4.on()
            print("N??chstes Level beginnt in 2 Sekunden!")
            sleep(1)
            Settings.led1.on()
            Settings.led5.on()
            print("N??chstes Level beginnt in 1 Sekunde!")
            sleep(1)
            Settings.led1.off()
            Settings.led2.off()
            Settings.led3.off()
            Settings.led4.off()
            Settings.led5.off()
            self.sequence = []
            self.allow_input = False
                
    def increase_difficulty(self):
        self.led_length += 1
        self.time * 0.8
        
    def reset_level(self):
        self.led_length = 5
        self.time = 0.5
        Settings.led1.on()
        Settings.led2.on()
        Settings.led3.on()
        Settings.led4.on()
        Settings.led5.on()
        print("Das Level startet sich in 3 Sekunden neu!")
        sleep(1)
        Settings.led1.off()
        Settings.led5.off()
        print("Das Level startet sich in 2 Sekunden neu!")
        sleep(1)
        Settings.led2.off()
        Settings.led4.off()
        print("Das Level startet sich in 1 Sekunde neu!")
        sleep(1)
        Settings.led3.off()
        self.sequence = []
        self.allow_input = False
            
    def wait_for_input(self):
        self.input_position = 0
        self.allow_input = True
        while self.allow_input:
            sleep(0.1)

game = Game()
game.run()
