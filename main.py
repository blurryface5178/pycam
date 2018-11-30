import cv2
import QR as qrFinder
import color as colorFinder
#import color_transfer as transfer

from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
import imutils

#import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

#for pc
#frame =  cv2.VideoCapture(0)

#for pi
camera = PiCamera()
camera.resolution = (320,2400)
camera.framerate = 32
rawCapture = PiRGBArray(camera, resolution=(320,240), framerate=32)
#GPIO.setmode(GPIO.BOARD)
time.sleep(0.5)
    
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):  
    #val, image = frame.read()

    image = frame.array

#    image = cv2.flip(image,1)
    send_img = image.copy()

    cv2.imshow("Image",image)

    color = colorFinder.lookForQR(send_img)
    #white=0, black=1, red=2, blue=3, green=4
    if(color==1):
        value = qrFinder.findQrcode(image)
        if(value):
            print("QR="+value)
    else:
        print(color)

    rawCapture.truncate(0)
    if (cv2.waitKey(1) & 0xFF==27):
        break
	

cv2.destroyAllWindows()
#frame.release()