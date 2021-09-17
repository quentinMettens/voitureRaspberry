import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import time
import threading
from servo import Servo
from Motor import Motor

class CapteurUltraSons(threading.Thread):
    
    def __init__(self, sonar, recept, distanceObstacle):
        threading.Thread.__init__(self)
        self.pinSonar = sonar  
        self.pinRecept = recept 
        self.distanceObstacle = distanceObstacle

  
    def cleanup(self):
        GPIO.cleanup()

    def getDistance(self):

        while True : 

            """Sortie"""
            GPIO.setup(self.pinRecept, GPIO.OUT)

            """Envoie une impulsion de 10 microseconde"""
            GPIO.output(self.pinRecept, True)
            time.sleep(0.00001)
            GPIO.output(self.pinRecept, False)

            start = time.time()
            count = time.time()

            """Entree"""
            GPIO.setup(self.pinSonar,GPIO.IN)

            """Sauvegarde le temps de depart de l'impulsion qui a ete emise """
            while GPIO.input(self.pinSonar)==0 and time.time()-count<0.1:
                start = time.time()

            count=time.time()
            stop=count

            while GPIO.input(self.pinSonar)==1 and time.time()-count<0.1:
                """Sauvegarde le temps d'arrivee de l'impulsion """
                stop = time.time()

            """Calcul la difference de temps entre l'emission de l'impulsion et de la reception"""
            elapsed = stop-start

            """Multiplication du temps par la vitesse du son"""
            distance = elapsed * 34000
            distance = distance / 2

            """Permet d'arrondir la variable distance a deux decimales"""
            distance = round(distance,2)

            


            if distance > 60 and self.pinSonar == 5 and self.pinRecept == 6:
                print ("Fonce")
                time.sleep(0.11) 
                mur.forwards(60)
                tourner.straight()
                tourner.straight()
            elif distance < 59 and distance > 50 and self.pinSonar == 5 and self.pinRecept == 6:
                print ("stop")
                time.sleep(0.5) 
                mur.forwards(25)
                tourner.straight()
            elif distance < 49 and distance > 15 and self.pinSonar == 5 and self.pinRecept == 6:
                print ("stop")
                mur.forwards(25)
                tourner.straight()
                time.sleep(0.5) 
                tourner.turn(40)
                time.sleep(2)
                tourner.straight()
                time.sleep(2)
                tourner.turn(160)
                time.sleep(2)
                tourner.straight()
                time.sleep(3)
                """tourner.turn(150)
                forwards(35)
                time.sleep(3)
                mur.forwards(25)
                tourner.turn(40)
                time.sleep(2.5)
                tourner.straight()
                time.sleep(4)"""
            elif distance < 15 and self.pinSonar == 5 and self.pinRecept == 6:
                print ("stop")
                mur.stop()
            else:
                pass



if __name__ == '__main__': # Program starts here

    capteurDevant = CapteurUltraSons(5,6,50)
    mur = Motor()
    tourner = Servo()
    try:
        capteurDevant.getDistance()
        capteurDevant.cleanup()
    except KeyboardInterrupt:
        print("testefin")

    except:
        print("Rate")
