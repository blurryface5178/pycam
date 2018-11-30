import cv2
import numpy as np

frame = cv2.VideoCapture(0)
while True:
    _, image = frame.read()

    grayscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(grayscale,50,255)

    #tot = cv2.bitwise_or(canny,r)

    cv2.imshow("Draw 1", canny)
    cv2.imshow("Draw",image[:,:,2])

    if(cv2.waitKey(1) == 27):
        break

cv2.destroyAllWindows()
frame.release()