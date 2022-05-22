"""Docstring"""
from Screens import splash_screen
from Utils.utilities import DpiAwareness
from Core import app

if __name__ == '__main__':
    temp =  app.APP()
    DpiAwareness(temp)
    temp.mainloop()
    
    # splash = splash_screen.SplashScreen()
    # DpiAwareness(splash)
    # splash.mainloop()
