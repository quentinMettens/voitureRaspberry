import board
import busio
import adafruit_pca9685
import RPi.GPIO as GPIO
from time import sleep

class Motor(object):

    i2c = busio.I2C(board.SCL, board.SDA)
    hat = adafruit_pca9685.PCA9685(i2c)
    hat.frequency = 50

    M0_En = 23   # pin4
    M0_A  = 17  # pin11
    M0_B  = 18  # pin12

    M1_En = 24   # pin4
    M1_A  = 27  # pin13
    M1_B  = 22  # pin15

    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)  # GPIO Numbering
        GPIO.setup(self.M0_En, GPIO.OUT)
        GPIO.setup(self.M0_A,  GPIO.OUT)
        GPIO.setup(self.M0_B,  GPIO.OUT)
        GPIO.setup(self.M1_En, GPIO.OUT)
        GPIO.setup(self.M1_A,  GPIO.OUT)
        GPIO.setup(self.M1_B,  GPIO.OUT)
        self.motorL = GPIO.PWM(self.M0_En, 100)
        self.motorR = GPIO.PWM(self.M1_En, 100)

    """ Goes Forwards for 'x' seconds at speed 'speed' """
    def forwards(self, speed = 100):
        GPIO.output(self.M0_A,  GPIO.HIGH)
        GPIO.output(self.M0_B,  GPIO.LOW)
        GPIO.output(self.M0_En, GPIO.HIGH)
        GPIO.output(self.M1_A,  GPIO.HIGH)
        GPIO.output(self.M1_B,  GPIO.LOW)
        GPIO.output(self.M1_En, GPIO.HIGH)
        self.motorL.start(speed)    # TODO : Tester si 0 < speed <= 100 ?
        self.motorR.start(speed)
        print("Go !")
        #sleep(t)
        #self.stop()
        print("stop !")

    """ Goes Backwards for 'time' seconds at speed 'speed' """
    def backwards(self, speed = 100):
        GPIO.output(self.M0_A,  GPIO.LOW)
        GPIO.output(self.M0_B,  GPIO.HIGH)
        GPIO.output(self.M0_En, GPIO.HIGH)
        GPIO.output(self.M1_A,  GPIO.LOW)
        GPIO.output(self.M1_B,  GPIO.HIGH)
        GPIO.output(self.M1_En, GPIO.HIGH)
        self.motorL.start(speed)    
        self.motorR.start(speed)
        print("Go !")
        #sleep(t)
        print("before stop !")
        #self.stop()
        print("stop !")


    """ Stops the car """
    def stop(self):
        print("stop")
        GPIO.output(self.M0_En, GPIO.LOW)
        GPIO.output(self.M1_En, GPIO.LOW)
        
if __name__ == '__main__': # Program starts here

    motorExec = Motor()
    try:
        print("test")
        motorExec.forwards(80)
        sleep(1)
        motorExec.forwards(50)
        sleep(1)
        motorExec.forwards(30)
        sleep(1)
        motorExec.forwards(10)
        sleep(1)
        motorExec.stop()
        print("Nice")
    except:
        print("Rate")