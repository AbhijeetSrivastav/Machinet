import time
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar

from Core import app
from Utils.utilities import ImageConfigurator, WinCenter


class SplashScreen(tk.Tk):
    def __init__(self):
        super(SplashScreen, self).__init__()

        "STYLING"
        self.FONT_WEIGHT = 'bold'
        self.FONT_STYLE = 'Calibri (Body)'
        self.FONT_SIZE = 18
        self.PRIMARY_COLOUR = 'White'
        self.SECONDARY_COLOUR = '#249794'

        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')

        "SCREEN PROPERTIES"
        self.WIDTH_SPLASH_SCREEN = app.WIDTH_APP_SCREEN
        self.HEIGHT_SPLASH_SCREEN = app.HEIGHT_APP_SCREEN - 100

        centrizer = WinCenter(self, self.WIDTH_SPLASH_SCREEN, self.HEIGHT_SPLASH_SCREEN)
        self.geometry("%dx%d+%d+%d" % (self.WIDTH_SPLASH_SCREEN, self.HEIGHT_SPLASH_SCREEN, centrizer[0], centrizer[1]))

        self.overrideredirect(True)  # removes the window options


        "WIDGETS"
        # creator_label = ttk.Label(self, text='PROGRAMMED', foreground=self.PRIMARY_COLOUR, background=self.SECONDARY_COLOUR,
        #                font=(self.FONT_STYLE, self.FONT_SIZE, self.FONT_WEIGHT))
        # creator_label.place(x=50, y=110)

        tk.Frame(self, width=self.WIDTH_SPLASH_SCREEN, height=self.HEIGHT_SPLASH_SCREEN,
                 background=self.SECONDARY_COLOUR).place(x=0, y=0)

        title_label = ttk.Label(self, text='MACHINET', foreground=self.PRIMARY_COLOUR, background=self.SECONDARY_COLOUR,
                                font=(self.FONT_STYLE, self.FONT_SIZE + 40, self.FONT_WEIGHT))
        title_label.place(x=50, y=200)

        sub_title_label = ttk.Label(self, text='An Auto ML Assist Tool', foreground=self.PRIMARY_COLOUR,
                                    background=self.SECONDARY_COLOUR,
                                    font=(self.FONT_STYLE, self.FONT_SIZE - 5, self.FONT_WEIGHT))
        sub_title_label.place(x=50, y=280)

        logo = ImageConfigurator('Assets/logo_test.jpg', dimension=(420, 320))
        logo_label = tk.Label(self, image=logo)
        logo_label.logo = logo
        logo_label.place(x=550, y=130)

        activate_button = tk.Button(self, width=10, height=1, borderwidth=5, justify="center", overrelief="raised",
                                    text='Get Started', command=self.bar, border=1,
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
