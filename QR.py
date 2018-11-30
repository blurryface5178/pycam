#import cv2
from pyzbar import pyzbar

def findQrcode(image):
    barcodes = pyzbar.decode(image)
    text = ""
    for barcode in barcodes:
#        (x, y, w, h) = barcode.rect
#        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)

#        text = barcode.data[0]-48
        print(barcode.data[0])

#    cv2.putText(image, str(text), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2)    cv2.imshow("Image", image)
    return text
