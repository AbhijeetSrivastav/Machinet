import tkinter as tk
from tkinter import ttk

from Core import app
from Screens.parameter_screen import LinearRegressionParaInfoScreen
import main
from Screens import welcome_screen, model_class_screen
from Utils import utilities
from Utils.utilities import fromRGB


class TaskBarFrame(tk.Frame):
    """Task bar at bottom"""

    def __init__(self, parent, width):
        super(TaskBarFrame, self).__init__(parent)

        self.master = parent

        self.config(border=5, bg=fromRGB(52, 52, 52), width=width)
        

        main_menu_button = ttk.Button(self, text='Main', command=self.MainMenu)
        main_menu_button.grid(row=0, column=0, sticky='e', rowspan=2)

        usage_button = ttk.Button(self, text='Usage', command=lambda: [welcome_screen.WelcomeFrame.WelcomeFrameDestruct(),Usage(parent=self.master).grid(row=0, column=1,sticky='e',rowspan=2)])
        usage_button.grid(row=0, column=1, sticky='e', rowspan=2)

        info_button = ttk.Button(self, text='Info', command=lambda: [welcome_screen.WelcomeFrame.WelcomeFrameDestruct(), Info(parent=self.master).grid(row=0, column=1,sticky='e',rowspan=2)])
        info_button.grid(row=0, column=2, sticky='e', rowspan=2)

        license_button = ttk.Button(self, text='License',
                                    command=lambda: [welcome_screen.WelcomeFrame.WelcomeFrameDestruct(), License(
                                        parent=self.master).grid(row=0, column=1, sticky='e', columnspan=2, rowspan=2)])
        license_button.grid(row=0, column=3, sticky='e', rowspan=2)

    def MainMenu(self):
        """Recreates the Welcome Frame and Task Bar Frame"""
        welcome_frame = welcome_screen.WelcomeFrame(parent=self.master, width=app.WIDTH_APP_SCREEN * 0.7, height=app.HEIGHT_APP_SCREEN)
        welcome_frame.grid(row=0, column=1, sticky='e', rowspan=2)

        model_type_frame = model_class_screen.ModelTypeFrame(parent=self, width=app.WIDTH_APP_SCREEN * 0.3, height=app.HEIGHT_APP_SCREEN)
        model_type_frame.grid(row=0, column=0, sticky='w', rowspan=1)

        task_bar_frame = TaskBarFrame(parent=self.master, width=app.WIDTH_APP_SCREEN * 0.7)
        task_bar_frame.grid(row=1, column=1, sticky='NSEW', columnspan=2)

class License(tk.Frame):
    def __init__(self, parent):
        super(License, self).__init__(parent)

        self.master = parent

        license_text = tk.Text(self, takefocus=True, font=('Leelawadee UI', 10),
                               cursor='cross', selectbackground='#B2FF59', width=90,
                               relief='groove', background=fromRGB(52, 52, 52),
                               foreground=fromRGB(251, 235, 88),
                               borderwidth=4, padx=7, pady=20, height=30, spacing2=4, wrap='word'
                               )
        license_text.grid(row=0, column=0, sticky='ew')
        license_text.insert('1.0', utilities.LICENSE)
        license_text['state'] = 'disabled'

        task_bar_frame = TaskBarFrame(parent=self.master, width=app.WIDTH_APP_SCREEN * 0.7)
        task_bar_frame.grid(row=1, column=1, sticky='NSEW', columnspan=2)

class Info(tk.Frame):
    def __init__(self, parent):
        super(Info, self).__init__(parent)

        self.master = parent

        info_text = tk.Text(self, takefocus=True, font=('Leelawadee UI', 10),
                            cursor='cross', selectbackground='#B2FF59', width=90,
                            relief='groove', background=fromRGB(52, 52, 52),
                            foreground=fromRGB(251, 235, 88),
                            borderwidth=4, padx=7, pady=20, height=30, spacing2=4, wrap='word'
                            )
        info_text.grid(row=0, column=0, sticky='ew')
        info_text.insert('1.0', utilities.INFO)
        info_text['state'] = 'disabled'

        task_bar_frame = TaskBarFrame(parent=self.master, width=app.WIDTH_APP_SCREEN * 0.7)
        task_bar_frame.grid(row=1, column=1, sticky='NSEW', columnspan=2)


class Usage(tk.Frame):
    def __init__(self, parent):
        super(Usage, self).__init__(parent)

        self.master = parent

        usage_text = tk.Text(self, takefocus=True, font=('Leelawadee UI', 10),
                             cursor='cross', selectbackground='#B2FF59', width=90,
                             relief='groove', background=fromRGB(52, 52, 52),
                             foreground=fromRGB(255, 255, 255),
                             borderwidth=4, padx=7, pady=20, height=30, spacing2=4, wrap='word'
                             )
        usage_text.grid(row=0, column=0, sticky='ew')
        usage_text.insert('1.0', utilities.USAGE)
        usage_text['state'] = 'disabled'

        task_bar_frame = TaskBarFrame(parent=self.master, width=app.WIDTH_APP_SCREEN * 0.7)
        task_bar_frame.grid(row=1, column=1, sticky='NSEW', columnspan=2)
