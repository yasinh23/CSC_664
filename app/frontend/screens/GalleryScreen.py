import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from app.backend.helpers import config, color
from app import constants
import os
from PIL import ImageTk, Image
from app.frontend.components import GalleryImage


class GalleryScreen(tk.Frame):
    # This page displays when users first startup program and/or when configurations aren't set
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.gallery_dir = config.get_gallery_dir()
        self.images = []
        entries = os.listdir(self.gallery_dir)

        if len(entries):
            img_path = f"{self.gallery_dir}/{entries[0]}"
            img = GalleryImage(img_path)
            img.set_delta_e()
            self.images.append(img)

            for entry in entries[1:]:
                img_path = f"{self.gallery_dir}/{entry}"

                img = GalleryImage(img_path)
                img.set_delta_e(ref=self.images[0].lab)
                self.images.append(img)

        if len(self.images):
            self.images.sort()
            self.populate_grid()

    def populate_grid(self):
        nr = 10  # number of rows
        nc = 10  # number of columns
        idx = 0

        photo_list = []

        for i in range(nr * nc):
            try:
                img = ImageTk.PhotoImage(self.images[idx].thumbnail)
                print(self.images[idx].lab)
            except IndexError:
                break
            lbl = tk.Label(self, image=img)
            lbl.img = img
            photo_list.append(lbl)
            photo_list[-1].grid(row=i // nc, column=i % nc)
            idx += 1

        # Display
