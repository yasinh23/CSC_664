import tkinter as tk
from app.constants import CONFIG_FILE, GALLERY_CARD_SIZE, GALLERY_ROWS, GALLERY_COL
import os
from PIL import ImageTk, Image
from app.frontend.components import GalleryImage


class Grid(tk.Frame):
    # This page displays when users first startup program and/or when configurations aren't set
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def build(self):
        self.gallery_dir = CONFIG_FILE.get_config('gallery_dir')
        self.images = []
        entries = os.listdir(self.gallery_dir)

        if len(entries):
            img_path = f"{self.gallery_dir}/{entries[0]}"
            img = GalleryImage(img_path)
            self.images.append(img)

            for entry in entries[1:]:
                img_path = f"{self.gallery_dir}/{entry}"
                img = GalleryImage(img_path)
                self.images.append(img)

        if len(self.images):
            self.images.sort()
            '''
            mini_grids = []
            while images:
                mini_grids.append()


            # pass list to mini grid class
            #
            '''
            self.populate_grid()

    def populate_grid(self):
        nc = GALLERY_COL  # number of columns
        idx = 0

        photo_list = []  # photo labels

        while True:
            try:
                img_obj = self.images[idx]
                img = ImageTk.PhotoImage(img_obj.img)
            except IndexError:
                break
            lbl = tk.Label(self, image=img)
            lbl.img = img
            photo_list.append(lbl)
            photo_list[-1].grid(row=idx // nc, column=idx % nc, padx=5)  # place last img of list on grid
            idx += 1

        # Display

# label date
# add to grid until photodate doesn't match label date
# make new grid underneath