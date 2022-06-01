import time
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Progressbar



class BuildingDialog(tk.Tk):
    def __init__(self):
        super(BuildingDialog, self).__init__()

        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')


        # self.HEIGHT = app.HEIGHT_APP_SCREEN * 0.2
        # self.WIDTH = app.WIDTH_APP_SCREEN * 0.2
        # centrizer = WinCenter(self, app.WIDTH_APP_SCREEN, app.HEIGHT_APP_SCREEN)
        # self.geometry("%dx%d+%d+%d" % (app.WIDTH_APP_SCREEN, app.HEIGHT_APP_SCREEN, centrizer[0], centrizer[1]))

        # self.overrideredirect(True)  # removes the window options

        # tk.Frame(self, width=app.WIDTH_APP_SCREEN * 0.2, height=app.HEIGHT_APP_SCREEN * 0.2,background=app.ACCENT_PINK).place(x=0, y=0)
        # logo = ImageConfigurator('Assets/logo_test.jpg', dimension=(120, 120))
        # logo_label = tk.Label(self, image=logo)
        # logo_label.logo = logo
        # logo_label.place(x=550, y=130)
        # title_label = ttk.Label(self, text='MACHINET', foreground=self.PRIMARY_COLOUR, background=self.SECONDARY_COLOUR,
        #                         font=(self.FONT_STYLE, self.FONT_SIZE + 40, self.FONT_WEIGHT))
        # title_label.place(x=50, y=200)
    
        loading_label = ttk.Label(self, text='Building...', foreground='black')
        loading_label.grid(column=0, row=2, columnspan=2, padx=100, pady=200)

        progress = ttk.Progressbar(self,orient='horizontal',mode='determinate',length=100)
        progress.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

        r = 0
        for i in range(100):
            progress['value'] = r
            self.update_idletasks()
            time.sleep(0.03)
            r = r + 1

        # Destroying itself after loading
        self.destroy()

if __name__ == "__main__":
    building_dialog = BuildingDialog()
    building_dialog.mainloop()