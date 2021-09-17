import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

IN_SENSOR = 20                             #Associate pin 38 to TRIG

GPIO.setup(IN_SENSOR,GPIO.IN)              #Set pin as GPIO in
i=0                                        #compteur de ligne
etatprecedent=False
while True:

    B=GPIO.input(IN_SENSOR)
    if(B==True and etatprecedent!=B):
        print("détection de la ligne d'arrivée")    #affichage lors d'une détecttion
        i+=1                                        #incrémentation du compteur
        print(i)                                    #affichage du compteur
    else: 
        print("piste du circuit")
    etatprecedent=B
    time.sleep(1)                            #Delay of 1 second
  
