"""
    la librairie est trop complexe pour en faire de la POO, nous n'avons donc pas pu utiliser ce script
"""

import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time
import Motor

kit = ServoKit(channels=16)

class Direction(object):
    def __init__(self):
        pass
    """ Turns Left 0 < 'rotation' < 90 """
    def turnLeft(self, rotation = 10):
        # Permet de faire tourner les roues vers la gauche
        if(rotation>0 and rotation<90):
            print("2")
            print(90-rotation)
            kit.servo[0].angle = 90 
            print(kit.servo[0].angle)
        elif rotation == 0 or rotation == 90:
            pass    # TODO : Test Resultat de 'pass' car ici pas de boucle
            # Objectif : Sortir de la fonction sans rien faire
            # Autres possibilités : 'break' ou 'continue'
        """
        else:
            t = t - 90 # TODO : Test si crash car instanciation d'une valeur déjà existante
            turnRight(rotation, t)
            break   # TODO : Test si 'break' sort de la fonction comme attendu

        # Permet d'avancer pendant t secondes avec les roues tournées
        #forwards(t)
        """
        # Permet de recentrer les roues
        kit.servo[0].angle = 90

    """ Turns Right 90 < 'rturn' < 180 """
    def turnRight(self, rotation = 10):

        #Permet de faire tourner les roues vers la droite
        if(rotation > 0 and rotation < 90):
            kit.servo[0].angle = 90 + rotation
        elif rotation == 0 or rotation == 90:
            pass    # TODO : Test Resultat de 'pass' car ici pas de boucle
            # Objectif : Sortir de la fonction sans rien faire
            # Autres possibilités : 'break' ou 'continue'
        """
        else:
            t = t - 90  # TODO : Test si crash car instanciation d'une valeur déjà existante
            turnLeft(rotation, t)   # TODO : Test si 'break' sort de la fonction comme attendu

        # Permet d'avancer pendant t secondes avec les roues tournées
        # forwards(t)
        """
        # Permet de recentrer les roues
        kit.servo[0].angle = 90
if __name__ == "__main__":

    direc = Direction()
    try:
        print("test")
        direc.turnLeft(50)
        direc.turnRight(40)
        print("Nice")
    except KeyboardInterrupt:
        print("CTRL+C")
    except:
        print("Rate")
