from Servo import Servo
import threading
import RPi.GPIO as GPIO
import time
import adafruit_pca9685
import board
import busio


class CapteurUltraSons(threading.Thread):

    def __init__(self, sonar, recept, distanceObstacle):
        threading.Thread.__init__(self)
        self.pinSonar = sonar  
        self.pinRecept = recept 
        self.distanceObstacle = distanceObstacle
  
    def cleanup(self):
        GPIO.cleanup()

    def getDistance(self):
        GPIO.setmode(GPIO.BCM)
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
    """
    def run (self):
        print ("Run - ", self.pinSonar, self.pinRecept)       
        self.getDistance()
        self.cleanup()
    """
class InfraredSensor (object):
    
    def __init__(self):                               #Super Constructor
        
        GPIO.setmode(GPIO.BCM)                   #Set GPIO BCM numbering 
        self.IN_SENSOR = 20                             #Associate pin 38 to TRIG
        GPIO.setup(self.IN_SENSOR,GPIO.IN)              #Set pin as GPIO in
    
    def caption(self):
       
        stp=False                                   #set the return to stop the car
        i=0                                        #Line counter
        print("Entrer un nombre de tour:")
        cpt=input()                                 #Store the number of loop to do
        cpt=int(cpt)
        etatprecedent=False                        #Boolean to don't count the same line
        while True:                                 #infinte loop

            B=GPIO.input(self.IN_SENSOR)                    #Safe the state of the IS
            if(B==True and etatprecedent!=B):               #condition
                i+=1                                        #Counter increment
                if(i>1):
                    print("détection de la ligne d'arrivée")    #Print line detection                
                    print(i-1)                                    #Print counter
                
            if(i-1==cpt):
                stp=True
                avancer.stop()
                break
        
            etatprecedent=B                             #Safe the previously state
            time.sleep(0.1)                            #Delay of 1 second
        return stp                                 #Stop the car at the number set by the user
    
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
        
        GPIO.setmode(GPIO.BCM) # GPIO Numbering
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






    #"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__ == '__main__': # Program starts here

    avancer = Motor()                                   #objet moteur
    tourner = Servo()                                   #objet servo
    avancer.forwards(100)
    capteurinfra = InfraredSensor()                       #capteur infrarouge
    capteurGauche = CapteurUltraSons(9,11,100)
    capteurDevant = CapteurUltraSons(5,6,60)
    while True:
        distancegauche = capteurGauche.getDistance()
        distancedevant = capteurDevant.getDistance()
        capteurDevant.cleanup()
        capteurGauche.cleanup()
        #capteurinfra.caption()


        if distancedevant < 15:                  #capteur devant
            print ("faut tourner à droite")                   
            if distancegauche < 15:             #capteur gauche
                print ("Ecarte Mur Gauche")
                time.sleep(0.11) 
                avancer.forwards(40)
                tourner.turn(130)

        if distancegauche > 70:
            print ("vers Mur Gauche")
            time.sleep(0.11) 
            print(distancegauche)
            avancer.forwards(40)
            tourner.turn(85)
        elif distancegauche > 50:
            print ("vers Mur Gauche")
            time.sleep(0.11) 
            avancer.forwards(30)
            tourner.turn(85)
        elif distancegauche > 36:
            print ("vers Mur Gauche")
            time.sleep(0.11) 
            print (distancegauche)
            avancer.forwards(20)
            tourner.turn(88)
        elif distancegauche > 31:
            print ("vers Mur Gauche")
            avancer.forwards(20)
        elif distancegauche < 30:
            print ("Ecarte Mur Gauche")
            time.sleep(0.11) 
            print (distancegauche)
            avancer.forwards(40)
            tourner.turn(130)
        else:
            avancer.forwards(40)
            tourner.straight()









