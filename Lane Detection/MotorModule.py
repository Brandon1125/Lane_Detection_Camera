"""
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
 
class Motor():
    def __init__(self,EnaA,In1A,In2A,EnaB,In1B,In2B):
        self.EnaA= EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB= EnaB
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.EnaA,GPIO.OUT);GPIO.setup(self.In1A,GPIO.OUT);GPIO.setup(self.In2A,GPIO.OUT)
        GPIO.setup(self.EnaB,GPIO.OUT);GPIO.setup(self.In1B,GPIO.OUT);GPIO.setup(self.In2B,GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnaA, 100);
        self.pwmB = GPIO.PWM(self.EnaB, 100);
        self.pwmA.start(0);
        self.pwmB.start(0);
        self.mySpeed=0
 
    def move(self,speed=0.5,turn=0,t=0):
        speed *=100
        turn *=70
        leftSpeed = speed-turn
        rightSpeed = speed+turn
 
        if leftSpeed>100: leftSpeed =100
        elif leftSpeed<-100: leftSpeed = -100
        if rightSpeed>100: rightSpeed =100
        elif rightSpeed<-100: rightSpeed = -100
        #print(leftSpeed,rightSpeed)
        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))
        if leftSpeed>0:GPIO.output(self.In1A,GPIO.HIGH);GPIO.output(self.In2A,GPIO.LOW)
        else:GPIO.output(self.In1A,GPIO.LOW);GPIO.output(self.In2A,GPIO.HIGH)
        if rightSpeed>0:GPIO.output(self.In1B,GPIO.HIGH);GPIO.output(self.In2B,GPIO.LOW)
        else:GPIO.output(self.In1B,GPIO.LOW);GPIO.output(self.In2B,GPIO.HIGH)
        sleep(t)
 
    def stop(self,t=0):
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);
        self.mySpeed=0
        sleep(t)
 
def main():
    motor.move(0.5,0,2)
    motor.stop(2)
    motor.move(-0.5,0,2)
    motor.stop(2)
    motor.move(0,0.5,2)
    motor.stop(2)
    motor.move(0,-0.5,2)
    motor.stop(2)
 
if __name__ == '__main__':
    motor= Motor(2,3,4,17,22,27)
    main()
"""

import RPi.GPIO as GPIO
from time import sleep # Se importa para producir retrasos para controlar la operación de motor.

GPIO.setmode(GPIO.BCM) # Configuramos el cómo nos referiremos a los pines del GPIO. BCM es un estándar
GPIO.setwarnings(False) # Desactiva las advertencias para evitar que llenen la consola.

#Motor(2,3,4,17,22,27)
class Motor(): # Funciones y variables relacionadas con el control del motor.
    # Pines para controlar la dirección y velocidad de cada motor.
    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B, EnaC, In1C, In2C, EnaD, In1D, In2D):
        # Configuración para ruedas traseras (A y B)
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        
        # Configuración para ruedas delanteras (C y D)
        self.EnaC = EnaC
        self.In1C = In1C
        self.In2C = In2C
        self.EnaD = EnaD
        self.In1D = In1D
        self.In2D = In2D

        # Configurar cada pin como una salida para enviar señales desde la Raspberry Pi hasta el motor
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        GPIO.setup(self.EnaC, GPIO.OUT)
        GPIO.setup(self.In1C, GPIO.OUT)
        GPIO.setup(self.In2C, GPIO.OUT)
        GPIO.setup(self.EnaD, GPIO.OUT)
        GPIO.setup(self.In1D, GPIO.OUT)
        GPIO.setup(self.In2D, GPIO.OUT)

        # El PWM permite controlar la velocidad del motor variando el ciclo de trabajo de la señal
        self.pwmA = GPIO.PWM(self.EnaA, 100)
        self.pwmB = GPIO.PWM(self.EnaB, 100)
        self.pwmC = GPIO.PWM(self.EnaC, 100)
        self.pwmD = GPIO.PWM(self.EnaD, 100)

        # El objetivo es empezar con un ciclo de trabajo del 0% para asegurar que el motor no se mueva hasta que se le indique
        self.pwmA.start(0)
        self.pwmB.start(0)
        self.pwmC.start(0)
        self.pwmD.start(0)

    # Método para controlar la velocidad y dirección
    def move(self, speed=0.5, turn=0, t=0):
        speed *= 100
        turn *= 70
        leftSpeed = speed - turn
        rightSpeed = speed + turn

        # Limitar velocidad
        if leftSpeed > 100: leftSpeed = 100
        elif leftSpeed < -100: leftSpeed = -100
        if rightSpeed > 100: rightSpeed = 100
        elif rightSpeed < -100: rightSpeed = -100

        # Cambiar el ciclo de trabajo de la señal de PWM para ajustar la velocidad del motor.
        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))
        self.pwmC.ChangeDutyCycle(abs(leftSpeed))
        self.pwmD.ChangeDutyCycle(abs(rightSpeed))

        # Configurar dirección
        self.setDirection(self.In1A, self.In2A, leftSpeed)
        self.setDirection(self.In1B, self.In2B, rightSpeed)
        self.setDirection(self.In1C, self.In2C, leftSpeed)
        self.setDirection(self.In1D, self.In2D, rightSpeed)

        sleep(t)

    # Separar la lógica que establece la dirección del motor para reutilizarla para cada motor.
    def setDirection(self, In1, In2, speed):
        if speed > 0:
            GPIO.output(In1, GPIO.HIGH)
            GPIO.output(In2, GPIO.LOW)
        else:
            GPIO.output(In1, GPIO.LOW)
            GPIO.output(In2, GPIO.HIGH)

    # Detiene todos los motores de manera inmediata.
    def stop(self, t=0):
        self.pwmA.ChangeDutyCycle(0) # Al establecer un ciclo de trabajo en 0%, se asegura que el motor se detenga.
        self.pwmB.ChangeDutyCycle(0)
        self.pwmC.ChangeDutyCycle(0)
        self.pwmD.ChangeDutyCycle(0)
        sleep(t)

if __name__ == '__main__':
    motor = Motor(2, 3, 4, 17, 22, 27, 5, 6, 13, 18, 23, 24)  # Asumiendo que estos son tus pines para las nuevas ruedas
    motor.move(0.5, 0, 2)
    motor.stop(2)
    motor.move(-0.5, 0, 2)
    motor.stop(2)
    motor.move(0, 0.5, 2)
    motor.stop(2)
    motor.move(0, -0.5, 2)
    motor.stop(2)

