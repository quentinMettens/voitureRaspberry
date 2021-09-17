import RPi.GPIO as GPIO                            #Import GPIO library
import time                                        #Import time library

class InfraredSensor (object):
    
    def __init__(self):                               #Super Constructor
        
        GPIO.setmode(GPIO.BCM)                          #Set GPIO BCM numbering 
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
                break
        
            etatprecedent=B                             #Safe the previously state
            time.sleep(0.1)                            #Delay of 1 second
        return stp                                 #Stop the car at the number set by the user
        
infrarouge= InfraredSensor()                            #New objet
infrarouge.caption()                                    #Run the function













  
