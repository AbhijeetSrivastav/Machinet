import tkinter as tk

from Screens import welcome_screen, model_class_screen, task_bar_screen

WIDTH = 1020
HEIGHT = 720


class APP(tk.Tk):
    def __init__(self):
        super(APP, self).__init__()

        self.resizable(False, False)
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=2)
        self.geometry('1020x720')
        self.title('Machine Learning Automation')

        model_type_frame = model_class_screen.ModelTypeFrame(parent=self, width=WIDTH * 0.3, height=HEIGHT)
        model_type_frame.grid(row=0, column=0, sticky='w', rowspan=1)

        welcome_frame = welcome_screen.WelcomeFrame(parent=self, width=WIDTH * 0.7, height=HEIGHT)
        welcome_frame.grid(row=0, column=1, sticky='e', rowspan=2)

        task_bar_frame = task_bar_screen.TaskBarFrame(parent=self)
        task_bar_frame.grid(row=1, column=1, sticky='NSEW', columnspan=2)



