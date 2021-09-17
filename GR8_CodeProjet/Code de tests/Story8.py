import time
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit

#Pin assiciation for motor
M0_En = 23  # pin4
M0_A  = 17  # pin11
M0_B  = 18  # pin12

M1_En = 24  # pin4
M1_A  = 27  # pin13
M1_B  = 22  # pin15
kit=ServoKit(channels=16)

def setup(): 
    GPIO.setmode(GPIO.BCM)  # GPIO Numbering
    GPIO.setup(M0_En, GPIO.OUT)
    GPIO.setup(M0_A,  GPIO.OUT)
    GPIO.setup(M0_B,  GPIO.OUT)
    GPIO.setup(M1_En, GPIO.OUT)
    GPIO.setup(M1_A,  GPIO.OUT)
    GPIO.setup(M1_B,  GPIO.OUT)
    
def forward():
    # Going Forwards
    GPIO.output(M0_A,  GPIO.HIGH)
    GPIO.output(M0_B,  GPIO.LOW)
    GPIO.output(M0_En, GPIO.HIGH)
    GPIO.output(M1_A,  GPIO.HIGH)
    GPIO.output(M1_B,  GPIO.LOW)
    GPIO.output(M1_En, GPIO.HIGH)

    time.sleep(2.25)

    # Stop
    GPIO.output(M0_En, GPIO.LOW)
    GPIO.output(M1_En, GPIO.LOW)
    
def backward():
    # Going Backwards
    GPIO.output(M0_A,  GPIO.LOW)
    GPIO.output(M0_B,  GPIO.HIGH)
    GPIO.output(M0_En, GPIO.HIGH)
    GPIO.output(M1_A,  GPIO.LOW)
    GPIO.output(M1_B,  GPIO.HIGH)
    GPIO.output(M1_En, GPIO.HIGH)

    time.sleep(2.25)

    # Stop
    GPIO.output(M0_En, GPIO.LOW)
    GPIO.output(M1_En, GPIO.LOW)

def tournerG():
    kit.servo[0].angle =0
    forward()
    kit.servo[0].angle = 90
    
def tournerD():
    kit.servo[0].angle =180
    forward()
    kit.servo[0].angle = 90
    
def tournerGA():
    kit.servo[0].angle =0
    backward()
    kit.servo[0].angle = 90
    
def tournerDA():
    kit.servo[0].angle =180
    backward()
    kit.servo[0].angle = 90

    
if __name__ == '__main__': # Program starts here
    setup()
    try:
        tournerD()
        tournerG()
        tournerDA()
        tournerGA()
    except KeyboardInterrupt:
       print("Fin du test")
        