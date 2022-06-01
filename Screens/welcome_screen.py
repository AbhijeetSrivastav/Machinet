from ctypes import alignment
import tkinter as tk
from tkinter import ttk

from Utils.utilities import ImageConfigurator, fromRGB
from Utils import utilities



class WelcomeFrame(tk.Frame):
    """Welcome screen"""

    def __init__(self, parent, width, height):
        super(WelcomeFrame, self).__init__()
        self.master = parent

        self.config(border=5, bg=fromRGB(239, 45, 86), width=width, height=height)
        self.grid_columnconfigure(1, weight=1)
        self.grid_propagate(0)

        global welcome_label
        welcome_label = ttk.Label(self, text='', anchor='center')
        welcome_label.grid(row=0, column=1)

        logo = ImageConfigurator('Assets/logo.png', dimension=(100, 100))
        logo_label = ttk.Label(self, image=logo)
        logo_label.logo = logo
        logo_label.grid(row=0, column=0)

        intro_text = tk.Text(self, takefocus=True, font=('Leelawadee UI', 10),
                               cursor='cross', selectbackground='#B2FF59', width=90,
                               relief='groove', background=fromRGB(52, 52, 52),
                               foreground=fromRGB(251, 235, 88),
                               borderwidth=4, padx=7, pady=20, height=30, spacing2=4, wrap='word'
                               )
        intro_text.grid(row=0, column=0, sticky='ew')
        intro_text.insert('1.0', utilities.INTRO)
        intro_text['state'] = 'disabled'
        
    @staticmethod
    def WelcomeFrameDestruct():
        for child in welcome_label.winfo_children():
            child.destroy()

        welcome_label.grid_forget()
