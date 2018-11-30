import cv2
import time
import QR as qrfinder

from picamera.array import PiRGBArray
from picamera import PiCamera
import time

#for pc
#frame =  cv2.VideoCapture(0)

#for pi
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera)
#GPIO.setmode(GPIO.BOARD)
time.sleep(0.5)
    
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):  
    #val, image = frame.read()

    image = frame.array

    value = qrfinder.findQrcode(image)
    print(value)

    rawCapture.truncate(0)
    if (cv2.waitKey(1) & 0xFF==27):
        break
