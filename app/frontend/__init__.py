import tkinter as tk
from .screens import screen_list, start_screen
from app.backend.helpers import config
from app import constants

LARGEFONT =("Verdana", 35)


class GUI(tk.Tk):
    # start app
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

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

            frame.grid(row=0, column=0, sticky="nsew")

        if config.config_exists(constants.CONFIG_PATH):
            # if config file exists
            print('config file exists')
        else:
            self.show_frame(start_screen)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
