import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from turtle import width

from Screens import welcome_screen, model_class_screen, task_bar_screen
from Utils.utilities import WinCenter, fromRGB

WIDTH_APP_SCREEN = 1020
HEIGHT_APP_SCREEN = 720
FONT_NORMAL = ('Leelawadee UI', 8)
FONT_BUTTON = ('Helvetica', 10)
ACCENT_PINK = fromRGB(239, 45, 86)
ACCENT_BLACK = fromRGB(52, 52, 52)
ACCENT_WHITE = fromRGB(250, 255, 253)

class APP(tk.Tk):
    def __init__(self):
        super(APP, self).__init__()

        "PROPERTIES"
        self.FONT_WEIGHT = 'bold'
        self.FONT_STYLE = 'Calibri (Body)'
        self.FONT_SIZE = 18
        self.PRIMARY_COLOUR = 'White'
        self.SECONDARY_COLOUR = '#249794'

        self.title('Machinet')
        centrizer = WinCenter(self, WIDTH_APP_SCREEN, HEIGHT_APP_SCREEN)
        self.geometry("%dx%d+%d+%d" % (WIDTH_APP_SCREEN, HEIGHT_APP_SCREEN, centrizer[0], centrizer[1]))
        self.resizable(False, False)
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=2)



        model_type_frame = model_class_screen.ModelTypeFrame(parent=self, width=WIDTH_APP_SCREEN * 0.3,
                                                             height=HEIGHT_APP_SCREEN)
        model_type_frame.grid(row=0, column=0, sticky='NSEW', rowspan=2)

        welcome_frame = welcome_screen.WelcomeFrame(parent=self, width=WIDTH_APP_SCREEN * 0.7, height=HEIGHT_APP_SCREEN)
        welcome_frame.grid(row=0, column=1, sticky='NSEW')

        task_bar_frame = task_bar_screen.TaskBarFrame(parent=self, width= WIDTH_APP_SCREEN * 0.7)
        task_bar_frame.grid(row=1, column=1, sticky='NSEW')
