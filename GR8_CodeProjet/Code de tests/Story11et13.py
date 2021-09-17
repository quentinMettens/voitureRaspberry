import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library

GPIO.setmode(GPIO.BCM)                      # GPIO Numbering

M0_En = 23  # pin4
M0_A  = 17  # pin11
M0_B  = 18  # pin12

M1_En = 24  # pin4
M1_A  = 27  # pin13
M1_B  = 22  # pin15

GPIO.setup(M0_En, GPIO.OUT)
GPIO.setup(M0_A,  GPIO.OUT)
GPIO.setup(M0_B,  GPIO.OUT)
GPIO.setup(M1_En, GPIO.OUT)
GPIO.setup(M1_A,  GPIO.OUT)
GPIO.setup(M1_B,  GPIO.OUT)


IN_SENSOR = 20                               #Associate pin 38 to TRIG
GPIO.setup(IN_SENSOR,GPIO.IN)              #Set pin as GPIO in

def forward():
    # Going Forwards
    GPIO.output(M0_A,  GPIO.HIGH)
    GPIO.output(M0_B,  GPIO.LOW)
    GPIO.output(M0_En, GPIO.HIGH)
    GPIO.output(M1_A,  GPIO.HIGH)
    GPIO.output(M1_B,  GPIO.LOW)
    GPIO.output(M1_En, GPIO.HIGH)
    
def stop():
    # Stop
    GPIO.output(M0_En, GPIO.LOW)
    GPIO.output(M1_En, GPIO.LOW)

forward()
i=0                                        #Line counter
print("Entrer un nombre de tour:")
cpt=input()                                 #Store the number of loop to do
cpt=int(cpt)
etatprecedent=False                        #Boolean to don't count the same line
while True:                                 #infinte loop

    B=GPIO.input(IN_SENSOR)                    #Safe the state of the IS
    if(B==True and etatprecedent!=B):               #condition
        i+=1                                        #Counter increment
        if(i>1):
            print("détection de la ligne d'arrivée")    #Print line detection                
            print(i-1)                                    #Print counter
                
    if(i-1==cpt):
        print("Nombre de tour effectués")
        stop()
        break
        
        etatprecedent=B                             #Safe the previously state
        time.sleep(0.1)                            #Delay of 1 second