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

        self.WIDTH_SPLASH_SCREEN = 427
        self.HEIGHT_SPLASH_SCREEN = 250
        self.PIXEL_COUNT_WIDTH = self.winfo_screenwidth()
        self.PIXEL_COUNT_HEIGHT = self.winfo_screenheight()
        x_coordinate = (self.PIXEL_COUNT_WIDTH / 2) - (self.WIDTH_SPLASH_SCREEN / 2)
        y_coordinate = (self.PIXEL_COUNT_HEIGHT / 2) - (self.HEIGHT_SPLASH_SCREEN / 2)
        self.geometry("%dx%d+%d+%d" % (self.WIDTH_SPLASH_SCREEN, self.HEIGHT_SPLASH_SCREEN, x_coordinate, y_coordinate))

        self.overrideredirect(1)

        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
        self.progress = Progressbar(self, style="red.Horizontal.TProgressbar", orient="horizontal", length=500,
                                    mode='determinate', )

        self.progress.place(x=-10, y=235)

        l1 = ttk.Label(self, text='SPLASH', foreground=self.PRIMARY_COLOUR, background=self.SECONDARY_COLOUR,
                       font=(self.FONT_STYLE, self.FONT_SIZE, self.FONT_WEIGHT))
        l1.place(x=50, y=80)

        l2 = ttk.Label(self, text='SCREEN', foreground=self.PRIMARY_COLOUR, background=self.SECONDARY_COLOUR,
                       font=(self.FONT_STYLE, self.FONT_SIZE, self.FONT_WEIGHT))
        l2.place(x=155, y=82)

        l3 = ttk.Label(self, text='PROGRAMMED', foreground=self.PRIMARY_COLOUR, background=self.SECONDARY_COLOUR,
                       font=(self.FONT_STYLE, self.FONT_SIZE, self.FONT_WEIGHT))
        l3.place(x=50, y=110)

        tk.Frame(self, width=427, height=241, background=self.SECONDARY_COLOUR).place(x=0, y=0)

        b1 = tk.Button(self, width=10, height=1, text='Get Started', command=self.bar, border=0,
                       foreground=self.SECONDARY_COLOUR,
                       background=self.PRIMARY_COLOUR)
        b1.place(x=170, y=200)

    def bar(self):
        l4 = ttk.Label(self, text='Loading...', foreground='white', background=self.PRIMARY_COLOUR,
                       font=(self.FONT_STYLE, 10, self.FONT_WEIGHT))
        l4.place(x=18, y=210)

        r = 0
        for i in range(100):
            self.progress['value'] = r
            self.update_idletasks()
            time.sleep(0.03)
            r = r + 1

        # Destroying the splash window and opeing app
        self.destroy()
        app.APP()
