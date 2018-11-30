import cv2
import numpy as np

kernel = np.ones((21,21),np.uint8)
count = 0

image = cv2.imread("maze.png")
cv2.imshow("Original",image)
#image = cv2.medianBlur(image,3)
empty = np.zeros((image.shape),np.uint8)

image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
_, image_thresh = cv2.threshold(image_gray,50,255,cv2.THRESH_BINARY_INV)

_, contours,_ = cv2.findContours(image_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    diff = cv2.drawContours(empty, contours,count,(255,255,255),2)
    diff = cv2.bitwise_not(diff)
    diff[np.where((diff==[0,0,0]).all(axis=2))] = [0,0,255]

    cv2.imshow(str(count),diff)
    final_image = cv2.bitwise_and(diff,image)
    cv2.imshow("Image"+str(count),final_image)

    count = count + 1

cv2.waitKey(0)
