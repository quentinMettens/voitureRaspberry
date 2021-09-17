from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
kit = ServoKit(channels=16)

class Servo:
    def __init__(self):
        self.angle = 90

    def turn(self, x):
        self.angle = x
        kit.servo[0].angle = self.angle

    def straight(self):
        self.angle = 92
        kit.servo[0].angle = self.angle

