import RPi.GPIO as GPIO
import time 
import demitour
import threading
from Motor import Motor
from Sovor import Servo


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



class CapteurUltraSons(threading.Thread):
    avancer = Motor()
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

            if distance <= 60 and self.pinSonar == 5 and self.pinRecept == 6:      
                print ("Distance:",distance - 0.5,"cm", "Obstacle detecte-devant")  
                time.sleep(0.1) 
                
            
            elif distance > 60 and self.pinSonar == 5 and self.pinRecept == 6:
                print ("Aucun soucis-devant")                   
                time.sleep(0.5)
                

                

            if distance < self.distanceObstacle and self.pinSonar == 19 and self.pinRecept == 26:
                print ("Distance:",distance - 0.5,"cm", "Obstacle detecte-Droite")
                time.sleep(0.5) 

            elif distance > self.distanceObstacle and self.pinSonar == 19 and self.pinRecept == 26:
                print ("Aucun soucis-Droite")
                time.sleep(0.5)


    
            if distance < 10 and self.pinSonar == 9 and self.pinRecept == 11:
                print ("Ecarte Mur Gauche")



            if distance > 10 and self.pinSonar == 9 and self.pinRecept == 11:
                print("Fonce vers le mur Gauche")


            if distance > 70 and distance < 200 and self.pinSonar == 9 and self.pinRecept == 11:
                print ("vers Mur Gauche")
                time.sleep(0.11) 
                print (distance)
                moteur.forwards(40)
                tourner.turn(85)
            elif distance > 50 and distance < 69 and self.pinSonar == 9 and self.pinRecept == 11:
                print ("vers Mur Gauche")
                time.sleep(0.11) 
                avancer.forwards(30)
                tourner.turn(85)
            elif distance > 36 and distance < 49 and self.pinSonar == 9 and self.pinRecept == 11:
                print ("vers Mur Gauche")
                time.sleep(0.11) 
                print (distance)
                avancer.forwards(20)
                tourner.turn(88)
            elif distance > 31 and distance < 35 and self.pinSonar == 9 and self.pinRecept == 11:
                print ("vers Mur Gauche")
                avancer.forwards(20)
            elif distance < 30 and self.pinSonar == 9 and self.pinRecept == 11:
                print ("Ecarte Mur Gauche")
                time.sleep(0.11) 
                print (distance)
                avancer.forwards(40)
                tourner.turn(130)
            else:
                avancer.forwards(40)
                tourner.straight()
        

            

    def run (self):
        print ("Run - ", self.pinSonar, self.pinRecept)       
        self.getDistance()
        self.cleanup()
    
"""
def main():
        thread1 = CapteurUltraSons(5,6,60)
        thread1.start()

        thread2 = CapteurUltraSons(19,26,60)
        thread2.start()

        thread3 = CapteurUltraSons(9,11,60)
        thread3.start()
"""