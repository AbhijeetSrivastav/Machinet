import tkinter as tk

import main
from Screens.parameter_screen import LinearRegressionParaInfoScreen


class RegressionModelSubTypeFrame(tk.Frame):
    """Contains Widget of Regression Model sub class"""

    def __init__(self, parent, width, height):
        super(RegressionModelSubTypeFrame, self).__init__(parent)

        self.config(width=width, height=height)
        self.grid_propagate(0)

        linear_reg = tk.Button(self, text='Linear', relief='raised', background='green', padx=3, pady=3,
                               font=('Helvetica', 10), command=lambda: self.RegressionModelParaDisplay('Linear'))
        linear_reg.grid(row=0, column=0, sticky='NSEW', padx=60, pady=20)

        multiple_reg = tk.Button(self, text='Multiple', relief='raised', background='green', padx=3, pady=3,
                                 font=('Helvetica', 10), command=lambda: self.RegressionModelParaDisplay('Multiple'))
        multiple_reg.grid(row=1, column=0, sticky='NSEW', padx=60, pady=20)

        polynomial_reg = tk.Button(self, text='Polynomial', relief='raised', background='green', padx=3, pady=3,
                                   font=('Helvetica', 10),
                                   command=lambda: self.RegressionModelParaDisplay('Polynomial'))
        polynomial_reg.grid(row=2, column=0, sticky='NSEW', padx=60, pady=20)

        decision_tree = tk.Button(self, text='Decision Tree', relief='raised', background='green', padx=3, pady=3,
                                  font=('Helvetica', 10),
                                  command=lambda: self.RegressionModelParaDisplay('Decision Tree'))
        decision_tree.grid(row=1, column=0, sticky='NSEW', padx=60, pady=20)

        random_forest = tk.Button(self, text='Random Forest', relief='raised', background='green', padx=3, pady=3,
                                  font=('Helvetica', 10),
                                  command=lambda: self.RegressionModelParaDisplay('Random Forest'))
        random_forest.grid(row=2, column=0, sticky='NSEW', padx=60, pady=20)

    def RegressionModelParaDisplay(self, selected_model):
        if selected_model == "Linear":
            linear_parar_screen = LinearRegressionParaInfoScreen(parent=self, width=main.WIDTH * 0.7,
                                                                 height=main.HEIGHT)
            linear_parar_screen.grid(row=0, column=1, sticky='e', rowspan=2)