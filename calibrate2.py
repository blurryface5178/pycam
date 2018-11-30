import cv2
import numpy as np
from imutils.video.pivideostream import PiVideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO


def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.createTrackbar('H High','Trackbars',0,255,nothing)
cv2.createTrackbar('S High','Trackbars',0,255,nothing)
cv2.createTrackbar('V High','Trackbars',0,255,nothing)

cv2.createTrackbar('H Low','Trackbars',0,255,nothing)
cv2.createTrackbar('S Low','Trackbars',0,255,nothing)
cv2.createTrackbar('V Low','Trackbars',0,255,nothing)

if __name__ == '__main__':

	vs = PiVideoStream().start()
	GPIO.setmode(GPIO.BOARD)
	time.sleep(0.5)


	while True:
		try:
			src = vs.read()
			image = cv2.flip(src, 1)


			hh = cv2.getTrackbarPos('H High','Trackbars')
			sh = cv2.getTrackbarPos('S High', 'Trackbars')
			vh = cv2.getTrackbarPos('V High', 'Trackbars')

			hl = cv2.getTrackbarPos('H Low', 'Trackbars')
			sl = cv2.getTrackbarPos('S Low', 'Trackbars')
			vl = cv2.getTrackbarPos('V Low', 'Trackbars')

			upper = np.array([hh, sh, vh], np.uint8)
			lower = np.array([hl,sl,vl],np.uint8)

			thresholded = cv2.inRange(image, lower, upper)
			cv2.imshow("Original",image)
			cv2.imshow('Output',thresholded)

			if cv2.waitKey(1)==27:
				break
				
		except KeyboardInterrupt:
			break

	vs.stop()
	cv2.destroyAllWindows()