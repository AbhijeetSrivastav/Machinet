import tkinter as tk

from Core import app
from Screens.parameter_screen import LinearRegressionParaInfoScreen, PolynomialRegressionParaInfoScreen
from Utils.utilities import fromRGB


class RegressionModelSubTypeFrame(tk.Frame):
    """Contains Widget of Regression Model sub class"""

    def __init__(self, parent, width, height):
        super(RegressionModelSubTypeFrame, self).__init__(parent)

        self.config(width=width, height=height, background=fromRGB(52, 52, 52))
        self.grid_propagate(0)

        linear_reg = tk.Button(self, text='Linear', relief='raised', background='green', padx=3, pady=3,font=app.FONT_BUTTON, command=lambda: self.RegressionModelParaDisplay('Linear'))
        linear_reg.grid(row=0, column=0, sticky='EW', padx=30, pady=30)

        multiple_reg = tk.Button(self, text='Multiple', relief='raised', background='green', padx=3, pady=3,font=app.FONT_BUTTON, command=lambda: self.RegressionModelParaDisplay('Multiple'))
        multiple_reg.grid(row=1, column=0, sticky='EW', padx=30, pady=30)

        polynomial_reg = tk.Button(self, text='Polynomial', relief='raised', background='green', padx=3, pady=3,font=app.FONT_BUTTON,command=lambda: self.RegressionModelParaDisplay('Polynomial'))
        polynomial_reg.grid(row=2, column=0, sticky='EW', padx=30, pady=30)

        decision_tree = tk.Button(self, text='Decision Tree', relief='raised', background='green', padx=3, pady=3,font=('Helvetica', 10),command=lambda: self.RegressionModelParaDisplay('Decision Tree'))
        decision_tree.grid(row=3, column=0, sticky='EW', padx=30, pady=30)

        random_forest = tk.Button(self, text='Random Forest', relief='raised', background='green', padx=3, pady=3,font=app.FONT_BUTTON,command=lambda: self.RegressionModelParaDisplay('Random Forest'))
        random_forest.grid(row=4, column=0, sticky='EW', padx=30, pady=30)

    def RegressionModelParaDisplay(self, selected_model):
        if selected_model == "Linear":
            linear_para_screen = LinearRegressionParaInfoScreen(parent=self, width=app.WIDTH_APP_SCREEN * 0.7, height=app.HEIGHT_APP_SCREEN)
            linear_para_screen.grid(row=0, column=1, sticky='NSEW')
        elif selected_model == 'Polynomial':
            polynomial_para_screen = PolynomialRegressionParaInfoScreen(parent=self, width=app.WIDTH_APP_SCREEN * 0.7, height=app.HEIGHT_APP_SCREEN)
            polynomial_para_screen.grid(row=0, column=1, sticky='NSEW')
