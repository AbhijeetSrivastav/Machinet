import time
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar

from Core import app


class SplashScreen(tk.Tk):
    def __init__(self):
        super(SplashScreen, self).__init__()

        "PROPERTIES"
        self.FONT_WEIGHT = 'bold'
        self.FONT_STYLE = 'Calibri (Body)'
        self.FONT_SIZE = 18
        self.PRIMARY_COLOUR = 'White'
        self.SECONDARY_COLOUR = '#249794'

        self.WIDTH_SPLASH_SCREEN = app.WIDTH
        self.HEIGHT_SPLASH_SCREEN = app.HEIGHT - 100
        self.PIXEL_COUNT_WIDTH = self.winfo_screenwidth()
        self.PIXEL_COUNT_HEIGHT = self.winfo_screenheight()
        x_coordinate = (self.PIXEL_COUNT_WIDTH / 2) - (self.WIDTH_SPLASH_SCREEN / 2)
        y_coordinate = (self.PIXEL_COUNT_HEIGHT / 2) - (self.HEIGHT_SPLASH_SCREEN / 2)
        self.geometry("%dx%d+%d+%d" % (self.WIDTH_SPLASH_SCREEN, self.HEIGHT_SPLASH_SCREEN, x_coordinate, y_coordinate))

        self.overrideredirect(True)  # removes the window options

        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')

        # creator_label = ttk.Label(self, text='PROGRAMMED', foreground=self.PRIMARY_COLOUR, background=self.SECONDARY_COLOUR,
        #                font=(self.FONT_STYLE, self.FONT_SIZE, self.FONT_WEIGHT))
        # creator_label.place(x=50, y=110)

        tk.Frame(self, width=self.WIDTH_SPLASH_SCREEN, height=self.HEIGHT_SPLASH_SCREEN,
                 background=self.SECONDARY_COLOUR).place(x=0, y=0)

        title_label = ttk.Label(self, text='MACHINET', foreground=self.PRIMARY_COLOUR, background=self.SECONDARY_COLOUR,
                                font=(self.FONT_STYLE, self.FONT_SIZE + 40, self.FONT_WEIGHT))
        title_label.place(x=100, y=200)

        sub_title_label = ttk.Label(self, text='An Auto ML Assist Tool', foreground=self.PRIMARY_COLOUR,
                                    background=self.SECONDARY_COLOUR,
                                    font=(self.FONT_STYLE, self.FONT_SIZE - 5, self.FONT_WEIGHT))
        sub_title_label.place(x=100, y=280)

        activate_button = tk.Button(self, width=10, height=1, text='Get Started', command=self.bar, border=0,
                                    foreground=self.SECONDARY_COLOUR,
                                    background=self.PRIMARY_COLOUR)
        activate_button.place(x=450, y=520)

    def bar(self):
        loading_label = ttk.Label(self, text='Loading...', foreground=self.SECONDARY_COLOUR,
                                  background=self.PRIMARY_COLOUR,
                                  font=(self.FONT_STYLE, 11, self.FONT_WEIGHT))
        loading_label.place(x=3, y=self.HEIGHT_SPLASH_SCREEN - 42)

        progress = Progressbar(self, style="red.Horizontal.TProgressbar", orient="horizontal",
                               length=self.WIDTH_SPLASH_SCREEN,
                               mode='determinate')
        progress.place(x=0, y=self.HEIGHT_SPLASH_SCREEN - 18)

        r = 0
        for i in range(100):
            progress['value'] = r
            self.update_idletasks()
            time.sleep(0.03)
            r = r + 1

        # Destroying the splash window and opeing app
        self.destroy()
        app.APP()
