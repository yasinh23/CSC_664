from PIL import ImageTk, Image
from app.backend.helpers import color
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976

class GalleryImage:
    def __init__(self, path):
        self.path = path
        self.thumbnail = self.crop_image(Image.open(self.path))
        self.RGB_avg = color.get_RGB_average(color.get_color_pallete(self.thumbnail))
        self.lab = color.rgb2lab(self.RGB_avg)
        self.delta_e = None

    def __lt__(self, other):
        return self.delta_e < other.delta_e

    def crop_image(self, img):
        width, height = img.size

        # Setting the points for cropped image
        left = 4
        top = height / 5
        right = 154
        bottom = 3 * height / 5

        im1 = img.crop((left, top, right, bottom))
        newsize = (100, 100)
        im1 = im1.resize(newsize)
        return im1

    def set_delta_e(self, ref=None):
        if ref:
            # Reference color.
            color1 = LabColor(lab_l=ref[0], lab_a=ref[0], lab_b=ref[0])
            # Color to be compared to the reference.
            color2 = LabColor(lab_l=self.lab[0], lab_a=self.lab[1], lab_b=self.lab[2])
            # This is your delta E value as a float.
            self.delta_e = delta_e_cie1976(color1, color2)
        else:
            self.delta_e = 0
