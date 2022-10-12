import tkinter as tk
from .screens import screen_list, start_screen, gallery_screen
from app.constants import REQUIRED_CONFIGS, CONFIG_FILE

LARGEFONT =("Verdana", 35)


class GUI(tk.Tk):
    # start app
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.pack()
        container.pack()

        # frame map
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in screen_list:
            # create screen; App.container is parent. App is controller
            frame = F(container, self)

            # initializing frame of that object from
            # for loop
            self.frames[F] = frame

            frame.pack()

        if CONFIG_FILE.has_required_configs(REQUIRED_CONFIGS):
            print('available')
            self.show_frame(gallery_screen)
        else:
            self.show_frame(start_screen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.build()
        frame.tkraise()
