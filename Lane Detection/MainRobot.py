from MotorModule import Motor
#from LaneDetectionModule import getLaneCurve
from LaneDetectionModule import camera
#import WebcamModule
import cv2
 
##################################################
#motor = Motor(2,3,4,17,22,27)
motor = Motor(2,3,4,17,22,27,5,6,13,18,23,24)

##################################################
 
def main():
 
    
    curveVal = camera()
 
    sen = 5  # SENSITIVITY
    maxVAl= 0.1 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    print("Desde main: ", curveVal)
    if curveVal>0:
        sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    motor.move(0.20,-curveVal*sen,0.05)
    cv2.waitKey(1)
     
 
if __name__ == '__main__':
    while True:
        main()