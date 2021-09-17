#Import for RPi
import board
import busio
import adafruit_pca9685
import RPi.GPIO as GPIO
from time import sleep
from adafruit_servokit import ServoKit


# Pins for Motor Driver Inputs

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
hat.frequency = 50
kit = ServoKit(channels=16)

M0_En = 23   # pin4
M0_A  = 17  # pin11
M0_B  = 18  # pin12

M1_En = 24   # pin4
M1_A  = 27  # pin13
M1_B  = 22  # pin15





def setup(): 
    GPIO.setmode(GPIO.BCM)  # GPIO Numbering
    GPIO.setup(M0_En, GPIO.OUT)
    GPIO.setup(M0_A,  GPIO.OUT)
    GPIO.setup(M0_B,  GPIO.OUT)
    GPIO.setup(M1_En, GPIO.OUT)
    GPIO.setup(M1_A,  GPIO.OUT)
    GPIO.setup(M1_B,  GPIO.OUT)


def loop():
    motor1GPIO = GPIO.PWM(M0_En, 100)
    motor2GPIO = GPIO.PWM(M1_En, 100)
    motor1GPIO.start(80)
    motor2GPIO.start(80)
    forwards()
    motor1GPIO.start(50)
    motor2GPIO.start(50)
    forwards()
    motor1GPIO.start(30)
    motor2GPIO.start(30)
    forwards()
    motor1GPIO.start(10)
    motor2GPIO.start(10)
    forwards()


# Vehicule forwards
def forwards():

    GPIO.output(M0_A,  GPIO.HIGH)
    GPIO.output(M0_B,  GPIO.LOW)
    #GPIO.output(M0_En, GPIO.HIGH)
    GPIO.output(M1_A,  GPIO.HIGH)
    GPIO.output(M1_B,  GPIO.LOW)
    #GPIO.output(M1_En, GPIO.HIGH)
# Vehicule backwards
def backwards():
    GPIO.output(M0_A,  GPIO.LOW)
    GPIO.output(M0_B,  GPIO.HIGH)
    GPIO.output(M0_En, GPIO.HIGH)
    GPIO.output(M1_A,  GPIO.LOW)
    GPIO.output(M1_B,  GPIO.HIGH)
    GPIO.output(M1_En, GPIO.HIGH)
#setup vitesse
def vitesse():
    motor1GPIO = GPIO.PWM(M0_En, 100)
    motor2GPIO = GPIO.PWM(M1_En, 100)
    motor1GPIO.start(40)
    motor2GPIO.start(40)
# Vehicule stop
def stop():
    GPIO.output(M0_En, GPIO.LOW)
    GPIO.output(M1_En, GPIO.LOW)

def tournerG():
    kit.servo[0].angle =0
    forwards()

def tournerGMur(angle):
    kit.servo[0].angle = angle
    forwards()

def tournerD(angle):
    kit.servo[0].angle = 180
    forwards()

def tournerDMur(angle):
    kit.servo[0].angle = angle
    forwards()

def roueDroite():
    kit.servo[0].angle =90
    forwards()

def tournerGA():
    kit.servo[0].angle =0
    backwards()
    
def tournerDA():
    kit.servo[0].angle =180
    backwards()
def destroy():
    GPIO.cleanup()

if __name__ == '__main__': # Program starts here

    setup()
    try:
        loop()
    except KeyboardInterrupt:
        stop()
        
        