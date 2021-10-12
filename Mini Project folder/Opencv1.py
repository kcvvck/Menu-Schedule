import numpy as np
import cv2
from matplotlib import pyplot as plt
from tkinter import Label, Button
import time


def opencvcam(self):
    z = 0

    faceCascade = cv2.CascadeClassifier('/Users/cv/Documents/haar-cascade-files-master/haarcascade_frontalface_alt.xml')
    

    cap = cv2.VideoCapture(0)

    while z <=5:
        # Capture frame-by-frame
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.01,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
        z += 1
        
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            
        

    noofppl = str(len(faces)*2)
    fdwaiting = Label(self, text ='Estimated waiting \n time: '+ noofppl + ' mins     ',
                  font=("royal acidbath", 20))
        

    fdwaiting.place(x = 1290, y = 150)
    # When everything is done, release the capture
    
    cv2.destroyAllWindows()