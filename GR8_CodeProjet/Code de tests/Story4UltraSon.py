import RPi.GPIO as GPIO
import time 


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class CapteurUltraSons():
    
    def __init__(self, sonar, recept, distanceObstacle):
        self.pinSonar = sonar  
        self.pinRecept = recept 
        self.distanceObstacle = distanceObstacle
  
    def cleanup(self):
        GPIO.cleanup()

    def getDistance(self):
        while True : 

            """Sortie"""
            GPIO.setup(self.pinRecept, GPIO.OUT)

            """Envoie une impulsion de 10 µs"""
            GPIO.output(self.pinRecept, True)
            time.sleep(0.00001)
            GPIO.output(self.pinRecept, False)

            start = time.time()
            count = time.time()

            """Entree"""
            GPIO.setup(self.pinSonar,GPIO.IN)

            """Sauvegarde le temps de départ de l'impulsion qui a été émise """
            while GPIO.input(self.pinSonar)==0 and time.time()-count<0.1:
                start = time.time()

            count=time.time()
            stop=count

            while GPIO.input(self.pinSonar)==1 and time.time()-count<0.1:
                """Sauvegarde le temps d'arrivée de l'impulsion """
                stop = time.time()

            """Calcul la différence de temps entre l'émission de l'impulsion et de la réception"""
            elapsed = stop-start

            """Multiplication du temps par la vitesse du son"""
            distance = elapsed * 34000
            distance = distance / 2

            """Permet d'arrondir la variable distance à deux décimales"""
            distance = round(distance,2)


            if distance < self.distanceObstacle and self.pinSonar == 29 and self.pinRecept == 31:      
                print ("Distance:",distance - 0.5,"cm")  
                print ("Obstacle detecte-devant")
                time.sleep(0.5) 
            
            elif distance > self.distanceObstacle and self.pinSonar == 29 and self.pinRecept == 31:
                print ("Aucun soucis-devant")                   
                time.sleep(0.5)

capteurDevant = CapteurUltraSons(29,31,25)
try:
    while True:
        capteurDevant.getDistance()
        capteurDevant.cleanup()
except KeyboardInterrupt : 
    print ("CTRL-C")