import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)


kit.servo[0].angle = 90
time.sleep(0.5)
kit.servo[0].angle =180
time.sleep(0.5)
kit.servo[0].angle = 20
time.sleep(0.5)
kit.servo[0].angle = 90
time.sleep(0.5)





