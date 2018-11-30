import cv2
import numpy as np
#import keyboard as key

#for pi
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
camera = PiCamera()
#camera.resolution = (640,480)
#camera.framerate = 32
rawCapture = PiRGBArray(camera)
#GPIO.setmode(GPIO.BOARD)
time.sleep(0.5)

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.createTrackbar('H High','Trackbars',0,255,nothing)
cv2.createTrackbar('S High','Trackbars',0,255,nothing)
cv2.createTrackbar('V High','Trackbars',0,255,nothing)

cv2.createTrackbar('H Low','Trackbars',0,255,nothing)
cv2.createTrackbar('S Low','Trackbars',0,255,nothing)
cv2.createTrackbar('V Low','Trackbars',0,255,nothing)

#frame = cv2.VideoCapture(0)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#    _, image = frame.read()

    image = frame.array
#    cv2.imshow("Original", image)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    hh = cv2.getTrackbarPos('H High','Trackbars')
    sh = cv2.getTrackbarPos('S High', 'Trackbars')
    vh = cv2.getTrackbarPos('V High', 'Trackbars')

    hl = cv2.getTrackbarPos('H Low', 'Trackbars')
    sl = cv2.getTrackbarPos('S Low', 'Trackbars')
    vl = cv2.getTrackbarPos('V Low', 'Trackbars')

    upper = np.array([hh, sh, vh], np.uint8)
    lower = np.array([hl,sl,vl],np.uint8)

    thresholded = cv2.inRange(image, lower, upper)

    cv2.imshow('Output',thresholded)

 #   if key.is_pressed('s'):
 #       file = open("Threshold.txt","a")
 #       values = [str(hh),str(sh),str(vh),str(hl),str(sl),str(vl)]
 #       file.write(str(values))
 #       print(values)
 #       file.close()

    rawCapture.truncate(0)

    if (cv2.waitKey(1) & 0xFF==27):
        break

#frame.release()
cv2.destroyAllWindows()