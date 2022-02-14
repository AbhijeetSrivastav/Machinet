"""Docstring"""
#from Core import app
from Screens import splash_screen
from Utils.utilities import DpiAwareness

if __name__ == '__main__':
    splash = splash_screen.SplashScreen()
    DpiAwareness(splash)
    splash.mainloop()

    # start = app.APP()
    # DpiAwareness(app)
    # start.mainloop()
