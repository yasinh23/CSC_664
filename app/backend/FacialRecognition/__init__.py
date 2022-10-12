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

# Displaying the image
cv2.imshow(window_name, img)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
