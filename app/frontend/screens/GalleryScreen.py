import tkinter as tk
from app.constants import CONFIG_FILE, GALLERY_CARD_SIZE, GALLERY_ROWS, GALLERY_COL
from PIL import ImageTk, Image
from app.frontend.frames.gallery import Grid, SortMenu


class GalleryScreen(tk.Frame):
    # This page displays when users first startup program and/or when configurations aren't set
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.sort_menu = SortMenu.SortMenu(self, controller)
        self.canvas = tk.Canvas(self, width=GALLERY_COL*GALLERY_CARD_SIZE, height=GALLERY_ROWS*GALLERY_CARD_SIZE)
        self.grid = Grid.Grid(self, controller)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.grid.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )



    def build(self):
        self.grid.build()
        self.grid.pack()
        self.sort_menu.pack(side=tk.LEFT, fill='y')
        self.canvas.pack(side=tk.LEFT, padx=(0, 50))
        self.scrollbar.pack(side=tk.RIGHT, fill='y')
        self.canvas.create_window((0, 0), window=self.grid, anchor="nw")



    def populate_grid(self):
        nr = GALLERY_ROWS  # number of rows
        nc = GALLERY_COL  # number of columns
        idx = 0

        photo_list = []

        for i in range(nr * nc):
            try:
                img = ImageTk.PhotoImage(self.images[idx].img)
            except IndexError:
                break
            lbl = tk.Label(self.grid, image=img)
            lbl.img = img
            photo_list.append(lbl)
            photo_list[-1].grid(row=i // nc, column=i % nc)
            idx += 1

        # Display
