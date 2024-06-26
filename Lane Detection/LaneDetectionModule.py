import cv2
import numpy as np
import utlis

curveList = []
avgVal = 10

def getLaneCurve(img, display = 0):
    
    imgCopy = img.copy()
    imgResult = img.copy()
    
    
    ########## STEP 1
    imgThres = utlis.thresholding(img)
    
    ########### STEP 2
    hT, wT, c = img.shape
    points = utlis.valTrackbars()
    imgWarp = utlis.warpImg(imgThres, points, wT, hT)
    imgWarpPoints = utlis.drawPoints(imgCopy, points)
    
    ########### STEP 3
    
    middlePoint, imgHist = utlis.getHistogram(imgWarp, display=True, minVal=0.5, region=4)
    curveAveragePoint, imgHist = utlis.getHistogram(imgWarp, display=True, minVal=0.9)
    curveRaw = curveAveragePoint - middlePoint
    
    ########## STEP 4
    curveList.append(curveRaw)
    if len(curveList) > avgVal:
        curveList.pop(0)
    curve = int( sum( curveList)/ len(curveList) ) 
    
    
    ######### STEP 5
    if display != 0:
       imgInvWarp = utlis.warpImg(imgWarp, points, wT, hT,inv = True)
       imgInvWarp = cv2.cvtColor(imgInvWarp,cv2.COLOR_GRAY2BGR)
       imgInvWarp[0:hT//3,0:wT] = 0,0,0
       imgLaneColor = np.zeros_like(img)
       imgLaneColor[:] = 0, 255, 0
       imgLaneColor = cv2.bitwise_and(imgInvWarp, imgLaneColor)
       imgResult = cv2.addWeighted(imgResult,1,imgLaneColor,1,0)
       midY = 450
       cv2.putText(imgResult,str(curve),(wT//2-80,85),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),3)
       cv2.line(imgResult,(wT//2,midY),(wT//2+(curve*3),midY),(255,0,255),5)
       cv2.line(imgResult, ((wT // 2 + (curve * 3)), midY-25), (wT // 2 + (curve * 3), midY+25), (0, 255, 0), 5)
       for x in range(-30, 30):
           w = wT // 20
           cv2.line(imgResult, (w * x + int(curve//50 ), midY-10),
                    (w * x + int(curve//50 ), midY+10), (0, 0, 255), 2)
       #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
       #cv2.putText(imgResult, 'FPS '+str(int(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (230,50,50), 3);
       if display == 2:
           imgStacked = utlis.stackImages(0.7,([img,imgWarpPoints,imgWarp],
                                         [imgHist,imgLaneColor,imgResult]))
           cv2.imshow('ImageStack',imgStacked)
       elif display == 1:
           cv2.imshow('Resutlt',imgResult)
    
    
    #cv2.imshow("Thresholding", imgThres)
    #cv2.imshow("Warp", imgWarp)
    #cv2.imshow("Warp Points", imgWarpPoints)
    #cv2.imshow("Warp", imgHist)
    
    ###NORMALIZATION
    curve = curve/100
    if curve>1: curve == 1
    if curve<-1:curve == -1
    
    return curve



def camera():
    
    cap = cv2.VideoCapture(0)
    initialTrackBarVals = [102, 80, 20, 214]
    utlis.initializeTrackbars(initialTrackBarVals)
    frameCounter = 0
    
    
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
        
        succes, img = cap.read()
        
        img = cv2.resize(img, (400, 200))
        #getLaneCurve(img)
        #curve = getLaneCurve(img, display = 0) # SHOW NOTING (FOR REAL TEST)
        #curve = getLaneCurve(img, display = 1) # SHOW ONLY ONE WINDOW
        curve = getLaneCurve(img, display = 1)
        #print(curve)
        
        #cv2.imshow("window", img)
        cv2.waitKey(1)
        return curve

