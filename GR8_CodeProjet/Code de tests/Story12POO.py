import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import time
import threading
from Servo import Servo
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
            return distance




if __name__ == '__main__': # Program starts here

    capteurGauche = CapteurUltraSons(9,11,100)
    capteurDevant = CapteurUltraSons(5,6,60)
    avancer = Motor()
    tourner = Servo()
    while True:
            distancegauche = capteurGauche.getDistance()
            time.sleep(0.1)
            print(distancegauche)
            distancedevant = capteurDevant.getDistance()
            time.sleep(0.1)
            print(distancedevant)
            if distancedevant < 15 and distancegauche < 15:
                print ("PJIDFGPSIDFJGBSDGJDOPFG")
                time.sleep(0.11) 
                avancer.forwards(40)
                tourner.turn(170)
            if distancegauche > 49:
                print ("vers Mur Gauche")
                time.sleep(0.11) 
                avancer.forwards(40)
                tourner.turn(45)
            elif distancegauche > 35:
                print ("vers Mur Gauche")
                time.sleep(0.11) 
                avancer.forwards(30)
                tourner.turn(78)
            elif distancegauche > 20:
                print ("vers Mur Gauche")
                time.sleep(0.11) 
                avancer.forwards(30)
                tourner.turn(80)
            elif distancegauche > 10:
                time.sleep(0.11) 
                avancer.forwards(20)
                tourner.turn(130)
            elif distancegauche < 10:
                print ("Ecarte Mur Gauche")
                time.sleep(0.11) 
                avancer.forwards(50)
                tourner.turn(140)
            else:
                avancer.forwards(40)
                tourner.straight()









