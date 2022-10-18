import cv2
import os
from app.backend.utils import randomize_mtime, gallery_as_path_list
#img = cv2.imread("/Users/yasinhagos/PycharmProjects/CSC_664/gallery/samuel_l_jackson_0.jpg")
#faces = model.detectMultiScale(img)
#directory = "/Users/yasinhagos/PycharmProjects/CSC_664/gallery"



model = cv2.CascadeClassifier("/Users/yasinhagos/PycharmProjects/CSC_664/gallery/haarcascade_frontalface_default.xml")
gal = gallery_as_path_list("/Users/yasinhagos/PycharmProjects/CSC_664/gallery")

for pics in gal:
    img = cv2.imread(pics)
    faces = model.detectMultiScale(img)
    for x, y, width, height in faces:
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 255), 2)
        cv2.imshow("Faces Found", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()