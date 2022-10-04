import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from app.backend.helpers import config
from app import constants

LARGEFONT =("Verdana", 35)


class StartPage(tk.Frame):
    # This page displays when users first startup program and/or when configurations aren't set
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.folder_path = tk.StringVar()
        self.config_file = None
        lbl1 = tk.Label(self, textvariable=self.folder_path)
        lbl1.grid(row=0, column=1)
        button2 = tk.Button(self, text="Browse", command=self.browse_button)
        button2.grid(row=0, column=3)
        button3 = tk.Button(self, text="Confirm", command=self.confirm_button)
        button3.grid(row=0, column=4)

    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        filename = filedialog.askdirectory()
        self.folder_path.set(filename)
        self.config_file = config.create_config(constants.CONFIG_PATH)

    def confirm_button(self):
        if self.config_file:
            d = config.load_config(self.config_file)
            d['gallery_folder'] = self.folder_path.get()
            config.write_config(self.config_file, d)

    def get_filepath(self):
        return self.folder_path
