import tkinter as tk

from Screens import welcome_screen, model_class_screen, task_bar_screen
from Utils.utilities import WinCenter

WIDTH_APP_SCREEN = 1020
HEIGHT_APP_SCREEN = 720


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
        model_type_frame.grid(row=0, column=0, sticky='w', rowspan=1)

        welcome_frame = welcome_screen.WelcomeFrame(parent=self, width=WIDTH_APP_SCREEN * 0.7, height=HEIGHT_APP_SCREEN)
        welcome_frame.grid(row=0, column=1, sticky='e', rowspan=2)

        task_bar_frame = task_bar_screen.TaskBarFrame(parent=self)
        task_bar_frame.grid(row=1, column=1, sticky='NSEW', columnspan=2)
