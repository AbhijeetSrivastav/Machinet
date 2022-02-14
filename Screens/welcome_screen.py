import tkinter as tk
from tkinter import ttk


class WelcomeFrame(tk.Frame):
    """Welcome screen"""

    def __init__(self, parent, width, height):
        super(WelcomeFrame, self).__init__()
        self.master = parent

        self.config(border=5, bg='black', width=width, height=height)
        self.grid_propagate(0)

        global welcome_label
        welcome_label = ttk.Label(self, text='Welcome to AUTO ML', anchor='center')
        welcome_label.grid(row=0, column=1)

    @staticmethod
    def WelcomeDestruct():
        for child in welcome_label.winfo_children():
            child.destroy()

        welcome_label.grid_forget()
