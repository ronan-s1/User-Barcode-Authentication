import cv2
import numpy as np
from pyzbar.pyzbar import decode


def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
     
    for obj in barcode:
        points = obj.polygon
        
        x, y, w, h = obj.rect
        
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        
        cv2.polylines(image, [pts], True, (255, 0, 0), 3)

        barcode_data = obj.data.decode("utf-8")
        barcode_type = obj.type
        
        string = f"Data: {barcode_data} | Type: {barcode_type}"
        
        cv2.putText(image, string, (x, y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
        print(string)


def video():
    #initialise web cam
    cap = cv2.VideoCapture(0)
    while True:
        #getting frames from web cam
        ret, frame = cap.read()
        decoder(frame)
        
        cv2.imshow("frame", frame)
        
        if cv2.waitKey(1) == ord("q"):
            break


def img():
    code_img = cv2.imread("qr.png")
    decoder(code_img)
    cv2.imshow("image", code_img) 
    cv2.waitKey(0)

