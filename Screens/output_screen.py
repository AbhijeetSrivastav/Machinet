import os
import tkinter as tk
from Core import app
from Utils.utilities import ImageConfigurator

class OutputScreen(tk.Tk):
    def __init__(self, result:list):
        super(OutputScreen, self).__init__()

        self.title('Report')
        self.config(background=app.ACCENT_PINK)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.iconbitmap('Assets/icon.ico')
        self.resizable(False, False)


        # FRAMES
        parameter_frame = tk.Frame(self, borderwidth=3, relief='groove', background=app.ACCENT_BLACK)
        parameter_frame.grid(row=0, column=0)
        parameter_frame.columnconfigure(0, weight=1)

        value_frame = tk.Frame(self, borderwidth=3, relief='sunken', background=app.ACCENT_BLACK)
        value_frame.grid(row=0, column=1)
        value_frame.columnconfigure(0, weight=1)

        actions_frame = tk.Frame(self, borderwidth=3, relief='raised', background=app.ACCENT_BLACK)
        actions_frame.grid(row=1, column=0, columnspan=2)
        actions_frame.columnconfigure(0, weight=1)
       

        for associatedFrame in self.winfo_children():
            associatedFrame.grid_configure(padx=60, pady=10, sticky='NSEW')


        # Parameters
        target_vector_label = tk.Label(parameter_frame, text='Predicted Value', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        target_vector_label.grid(row=0, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        regressor_coefficient_label = tk.Label(parameter_frame, text='Regressor Coefficient', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        regressor_coefficient_label.grid(row=1, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        regressor_intercept_label = tk.Label(parameter_frame, text='Regressor Intercept', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        regressor_intercept_label.grid(row=2, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        # VALUES
        target_vector_value_label = tk.Label(value_frame, text=result[0], anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        target_vector_value_label.grid(row=0,column=1, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        regressor_coefficient_value_label = tk.Label(value_frame, text=result[1], anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        regressor_coefficient_value_label.grid(row=1,column=1, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        regressor_intercept_value_label = tk.Label(value_frame, text=result[2], anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        regressor_intercept_value_label.grid(row=2,column=1, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')


        # ACTIONS
        save_results_button = tk.Button(actions_frame, text='Save Results',  font=app.FONT_NORMAL, justify='center', activebackground=app.ACCENT_PINK, relief='raised', anchor=tk.CENTER, border=3, command=lambda: generateReport())
        save_results_button.grid(row=3, column=0, padx=20, pady=2, ipadx=25, ipady=5, sticky='NSEW')


        def generateReport():
            directory = os.path.expanduser('~') + '\\Desktop'
            filePath = os.path.join(directory, 'simple_linear_regression_output.txt')
            with open(filePath, 'w') as file:
                file.write('----------------------------------- \n')
                file.write('| SIMPLE LINEAR REGRESSION REPORT | \n')
                file.write('----------------------------------- \n')
                file.write('Predicted Target Vector-->' + str(result[0]) + '\n')
                file.write('Regressor Coefficient-->' + str(result[1]) + '\n')
                file.write('Regressor Intercept-->' + str(result[2]) + '\n')
                file.close()