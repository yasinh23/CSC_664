import face_recognition
import imutils #imutils includes opencv functions
# from app.constants import CONFIG_FILE
# from app.backend import utils
import pickle
import time
import cv2
import os

def gallery_as_path_list(path):
    p = []

    for entry in os.listdir(path):
        p.append(f'{path}/{entry}')

    return p

gallery_dir = '/Users/fone/PycharmProjects/CSC_664/group_project/gallery'
image_paths = gallery_as_path_list(gallery_dir)
kEncodings = []
kNames = []

# Load the cascade
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

img = cv2.imread(image_paths[0])
window_name = 'image'

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, img)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)


'''
for p in image_paths:


    while True:
        # Read the frame
        _, img = img.read()
        img = cv2.imread(p)
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect     the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Display
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

# Release the VideoCapture object
cap.release()
'''