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

            


            if distance > 49  and self.pinSonar == 9 and self.pinRecept == 11:
                print ("vers Mur Gauche")
                time.sleep(0.11) 
                print (distance)
                avancer.forwards(40)
                tourner.turn(45)
            elif distance > 35 and distance < 49 and self.pinSonar == 9 and self.pinRecept == 11:
                print ("vers Mur Gauche")
                time.sleep(0.11) 
                avancer.forwards(30)
                tourner.turn(78)
            elif distance > 20 and distance < 35 and self.pinSonar == 9 and self.pinRecept == 11:
                print ("vers Mur Gauche")
                time.sleep(0.11) 
                print (distance)
                avancer.forwards(20)
                tourner.turn(80)
            elif distance > 10 and distance < 20 and self.pinSonar == 9 and self.pinRecept == 11:
                """print ("vers Mur Gauche")
                avancer.forwards(20)"""
                print ("Ecarte Mur Gauche")
                time.sleep(0.11) 
                print (distance)
                avancer.forwards(50)
                tourner.turn(130)
            elif distance < 10 and self.pinSonar == 9 and self.pinRecept == 11:
                print ("Ecarte Mur Gauche")
                time.sleep(0.11) 
                print (distance)
                avancer.forwards(50)
                tourner.turn(140)
            else:
                avancer.forwards(40)
                tourner.straight()



if __name__ == '__main__': # Program starts here

    capteurGauche = CapteurUltraSons(9,11,100)
    avancer = Motor()
    tourner = Servo()
    try:
        capteurGauche.getDistance()
        capteurGauche.cleanup()
    except KeyboardInterrupt:
        avancer.stop()

    except:
        print("Rate")









