import cv2
import numpy as np

lower_white = np.array([0, 0, 170], dtype=np.uint8)
upper_white = np.array([180, 17, 255], dtype=np.uint8)

lower_black = np.array([94,0,0],dtype=np.uint8)
upper_black = np.array([126,89,84],dtype=np.uint8)

lower_red = np.array([169,114,150],dtype=np.uint8)
upper_red = np.array([189,208,255],dtype=np.uint8)

lower_blue = np.array([98,141,107],dtype=np.uint8)
upper_blue = np.array([108,239,241],dtype=np.uint8)

lower_green = np.array([61,112,148],dtype=np.uint8)
upper_green = np.array([75,176,255],dtype=np.uint8)

#white=0, black=1, red=2, blue=3, green=4
thresholds=[lower_white,upper_white,lower_black,upper_black,lower_red,upper_red,lower_blue,upper_blue,lower_green, upper_green]

def return_contours(img):
    # img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # masked_frame = cv2.medianBlur(img2, 15, 0)
    # masked_frame = cv2.bilateralFilter(img2, 30, 200, 1)
    # _, thresh2 = cv2.threshold(img, 127, 255, 0)
    # #cv2.imshow('Output', thresh2)
    return cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

def findColor(src,color_code):
    lower,upper = thresholds[color_code*2], thresholds[color_code*2+1]

    #src_color=src
    src_color = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

    threshold_color = cv2.inRange(src_color,lower, upper)
    _, contours, hierarchy = cv2.findContours(threshold_color, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#    cv2.drawContours(src, contours, -1, (255, 137, 59), 1)

    if (len(contours) > 0):
        area_color = [cv2.contourArea(contour) for contour in contours]
        area_color = max(area_color)


#        show_and = cv2.bitwise_and(src,src,mask=threshold_color)
#        cv2.imshow("Thresh"+str(color_code),show_and)
#        return area_color
    else:
        return 0

def lookForQR(original_image):
    h, w, _ = original_image.shape
    #image = original_image
    image = original_image[int(h / 5):int(4 * h / 5), int(w / 5):int(4 * w / 5)]
#    cv2.imshow("Crop Image",image)

    area_black= findColor(image, 1)
    area_white= findColor(image,0)
    area_red= findColor(image, 2)
    area_blue= findColor(image, 3)
    area_green= findColor(image,4)

    all_area = [area_white,area_black,area_red,area_blue,area_green]

    color_is = all_area.index(max(all_area))

    return color_is