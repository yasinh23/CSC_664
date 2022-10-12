import os
from subprocess import call
from random import randrange
from datetime import datetime
import piexif


def gallery_as_path_list(path):
    p = []

    for entry in os.listdir(path):
        p.append(f'{path}/{entry}')

    return p


def randomize_mtime(path):
    month = randrange(1,12)
    day = randrange(1,30)
    year = randrange(2000,2020)
    d = datetime(year, month, day, 0, 0)
    epoch = d.timestamp()
    os.utime(path, (epoch, epoch))
    exif_dict = piexif.load(path)
    new_date = datetime(year, month, day, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, path)
