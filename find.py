import cv2
import RPi.GPIO as GPIO
import numpy as np
from imutils.video.pivideostream import PiVideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera


def detect_rectangle(rect_cnt):
	return cv2.boundingRect(rect_cnt)


def ycrcb_img_threshold(src):


	lower_white = np.array([white_h_low, white_s_low, white_v_low], dtype=np.uint8)
	upper_white = np.array([white_h_high, white_s_high ,white_v_high],dtype=np.uint8)

	lower_black = np.array([black_h_low, black_s_low, black_v_low], dtype=np.uint8)
	upper_black = np.array([black_h_high,black_s_high,black_v_high],dtype=np.uint8)

	gamma_adjusted = cv2.medianBlur(src,5)
	
	ycrcb_img = cv2.cvtColor(gamma_adjusted, cv2.COLOR_RGB2YCrCb)
	
	th3 = cv2.inRange(ycrcb_img,lower_white,upper_white)
	th4 = cv2.inRange(ycrcb_img,lower_black,upper_black)
	
	th5 = cv2.add(th3,th4)
	
	#th5 = cv2.bitwise_not(th5)			#inverting image
	
	cv2.imshow('the5', th5)
	
	smoothed = cv2.blur(th5,(8,8))
	
	return smoothed


def find_box(src):
	
	frame_threshold = ycrcb_img_threshold(src)

		
	img3, contours, hierarchy = cv2.findContours(frame_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	
	if (len(contours) > 0):
		indexOfBiggestContour = -1;
		sizeOfBiggestContour = 0;
		for i in range(len(contours)):
			if (len(contours[i]) > sizeOfBiggestContour):
				sizeOfBiggestContour = len(contours[i])
				indexOfBiggestContour = i

		for i in range(len(contours)):
		
			if (cv2.contourArea(contours[i]) > 1000):
				if (indexOfBiggestContour == i):

					cnt = contours[i]
					
					x,y,w,h = detect_rectangle(cnt)

					cv2.circle(src, (x, y), 10, (0, 255, 0), -1)

					cv2.drawContours(src, contours , indexOfBiggestContour, (0,0,255), 2)
					
					#M = cv2.moments(contours[indexOfBiggestContour])
					
					#cX = int(M["m10"] / M["m00"])
					#cY = int(M["m01"] / M["m00"])

					# if(abs(cX-x_height) < threshold_diffence):
					# 	x_avg = int((cX+x_height)/2)
					# 	y_avg = int((cY+y)/2)

					#x_avg = cX
					#y_avg = cY


	# draw the contour and center of the shape on the image
					#cv2.circle(src, (x_avg, y_avg), 10, (255,0,0), -1)
					#cv2.circle(src, (cX, cY), 7, (255, 255, 255), -1)
					
					if(not IS_IR_FIRED):
						motor_control_normal()
						search_mode_enabled = True
					else:
						if(y <= IR_RELEASE_THRESHOLD_HEIGHT):
							IS_IR_FIRED = False


			else:
				if(not IS_IR_FIRED):
					search_mode()	

	else:
		if(not IS_IR_FIRED):
			search_mode()
			
			
			
if __name__ == '__main__':
	vs = PiVideoStream().start()
	GPIO.setmode(GPIO.BOARD)
	time.sleep(0.5)

	while True:
	
		try:
			src = vs.read()
			src = cv2.flip(src, 1)
			#src = src[52:170, 0:320]

			find_box(image)

			
			
			if cv2.waitKey(1)==27:
				break
				
		except KeyboardInterrupt:
			break

	vs.stop()
	cv2.destroyAllWindows()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
