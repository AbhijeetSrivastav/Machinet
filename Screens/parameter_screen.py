import os
from re import S
import subprocess
import tkinter as tk
from tkinter import filedialog

from matplotlib import style
from Core import app
from Models.Regression.simple_linear_regression_model import LinearRegressionModel
from Models.Regression.polynomial_linear_regression import PolynomialRegressionModel


PATH_TO_NOTEPAD_EXE = 'C:\\Windows\\System32\\notepad.exe'

class LinearRegressionParaInfoScreen(tk.Frame):
    def __init__(self, parent, width, height):
        super(LinearRegressionParaInfoScreen, self).__init__()

        self.master = parent
        self.dataset_path = ''
        self.linear_regression_model = None

        self.config(background=app.ACCENT_PINK)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        # FRAMES
        labels_frame = tk.Frame(self, borderwidth=3, relief='groove', background=app.ACCENT_BLACK)
        labels_frame.grid(row=0, column=0)
        labels_frame.columnconfigure(0, weight=1)

        input_frame = tk.Frame(self, borderwidth=3, relief='sunken', background=app.ACCENT_BLACK)
        input_frame.grid(row=0, column=1)
        input_frame.columnconfigure(0, weight=1)

        actions_frame = tk.Frame(self, borderwidth=3, relief='raised', background=app.ACCENT_BLACK)
        actions_frame.grid(row=1, column=0, columnspan=2)
        actions_frame.columnconfigure(0, weight=1)
       

        for associatedFrame in self.winfo_children():
            associatedFrame.grid_configure(padx=60, pady=10, sticky='NSEW')


        # LABELS
        selected_dataset_label = tk.Label(labels_frame, text='Dataset', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        selected_dataset_label.grid(row=0, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        input_vector_begin_index_label = tk.Label(labels_frame, text='Input vector begin Index', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        input_vector_begin_index_label.grid(row=1, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        input_vector_end_index_label = tk.Label(labels_frame, text='Input Vector End Index', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        input_vector_end_index_label.grid(row=2, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        target_vector_index_label = tk.Label(labels_frame, text='Target Vector Index', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        target_vector_index_label.grid(row=3, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        test_size_label = tk.Label(labels_frame, text='Test Size', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        test_size_label.grid(row=4, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        graph_title_label = tk.Label(labels_frame, text='Graph Title', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        graph_title_label.grid(row=5, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        x_axis_label = tk.Label(labels_frame, text='X Label', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        x_axis_label.grid(row=6, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')
        
        y_axis_label = tk.Label(labels_frame, text='Y Label', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        y_axis_label.grid(row=7, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')
        
        training_data_point_colour_label = tk.Label(labels_frame, text='Train Point Colour', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        training_data_point_colour_label.grid(row=8, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        predicted_curve_colour = tk.Label(labels_frame, text='Predicted Curve Colour', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        predicted_curve_colour.grid(row=9, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')

        to_predict_value_label = tk.Label(labels_frame, text='Predict value for', anchor=tk.CENTER, borderwidth=4, font=app.FONT_NORMAL, justify='center', relief='ridge')
        to_predict_value_label.grid(row=10, column=0, padx=40, pady=10, ipadx=5, ipady=5, sticky='EW')


        # INPUTS
        self.dataset_selection_button = tk.Button(input_frame, text='Select Dataset', font=app.FONT_NORMAL, command=lambda: self.SelectDataset())
        self.dataset_selection_button.grid(row=0, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.input_vector_begin_index_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.input_vector_begin_index_input.grid(row=1, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.input_vector_end_index_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.input_vector_end_index_input.grid(row=2, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.target_vector_index_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.target_vector_index_input.grid(row=3, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.test_size_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.test_size_input.grid(row=4, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.graph_title_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.graph_title_input.grid(row=5, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.x_axis_label_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.x_axis_label_input.grid(row=6, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.y_axis_label_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.y_axis_label_input.grid(row=7, column=1,  padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.training_data_point_colour_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.training_data_point_colour_input.grid(row=8, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.predicted_curve_colour_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.predicted_curve_colour_input.grid(row=9, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')

        self.to_predict_value_input = tk.Entry(input_frame, justify='center', font=app.FONT_NORMAL)
        self.to_predict_value_input.grid(row=10, column=1, padx=15, pady=11, ipadx=5, ipady=5, sticky='EW')
        

        # ACTIONS
        train_button = tk.Button(actions_frame, text='Train',  font=app.FONT_NORMAL, justify='center', activebackground=app.ACCENT_PINK, relief='raised', anchor=tk.CENTER, border=3, command=lambda: self.Train())
        train_button.grid(row=11, column=0, padx=20, pady=2, ipadx=25, ipady=5, sticky='NSEW')

        predict_button = tk.Button(actions_frame, text='Predict', font=app.FONT_NORMAL, justify='center', activebackground=app.ACCENT_PINK, relief='raised', anchor=tk.CENTER, border=3, command=lambda: self.Predict())
        predict_button.grid(row=11, column=1, padx=20, pady=2, ipadx=25, ipady=5, sticky='NSEW')

        visualize_button = tk.Button(actions_frame, text='Visualize', font=app.FONT_NORMAL, justify='center', activebackground=app.ACCENT_PINK, relief='raised', anchor=tk.CENTER, border=3, command=lambda: self.Visualize())
        visualize_button.grid(row=11, column=2, padx=20, pady=2,  ipadx=25, ipady=5, sticky='NSEW')

        view_dataset_button = tk.Button(actions_frame, text='View Dataset', font=app.FONT_NORMAL, justify='center', activebackground=app.ACCENT_PINK, relief='raised', anchor=tk.CENTER, border=3, command=lambda: self.ViewDataset())
        view_dataset_button.grid(row=11, column=3, padx=20, pady=2,  ipadx=25, ipady=5, sticky='NSEW')

        template_button = tk.Button(actions_frame, text='Template', font=app.FONT_NORMAL, justify='center', activebackground=app.ACCENT_PINK, relief='raised', anchor=tk.CENTER, border=3, command=lambda: self.TemplateGenerator())
        template_button.grid(row=11, column=4, padx=20, pady=2,  ipadx=25, ipady=5, sticky='NSEW')


    def SelectDataset(self):
        self.dataset_path = filedialog.askopenfilename(initialdir="/", title="Dataset", filetypes=(("CSV files","*.csv*"),("all files", "*.*")))
        dataset_path_splitted = self.dataset_path.split('/')
        dataset_name = dataset_path_splitted[-1]
        self.dataset_selection_button.config(text=dataset_name)

    def Train(self):
        self.linear_regression_model = LinearRegressionModel(dataset=self.dataset_path, input_vector_begin_index=int(self.input_vector_begin_index_input.get()), input_vector_end_index=int(self.input_vector_end_index_input.get()), target_vector_index=int(self.target_vector_index_input.get()))
        self.linear_regression_model.Train(test_size=float(self.test_size_input.get()))

    def Predict(self):
        self.linear_regression_model.Predict()
        self.linear_regression_model.PredictValueFor(to_predict_value=int(self.to_predict_value_input.get()))

    def Visualize(self):
        self.linear_regression_model.VisualizeTrainSet(graph_title=self.graph_title_input.get(),xlabel=self.x_axis_label_input.get(),ylabel=self.y_axis_label_input.get(),train_point_colour=self.training_data_point_colour_input.get(),predicted_curve_colour=self.predicted_curve_colour_input.get())
        
        self.linear_regression_model.VisualizeTestSet(graph_title=self.graph_title_input.get(),xlabel=self.x_axis_label_input.get(),ylabel=self.y_axis_label_input.get(),train_point_colour=self.training_data_point_colour_input.get(),predicted_curve_colour=self.predicted_curve_colour_input.get())
    
    def ViewDataset(self):
        path_to_file = self.dataset_path
        subprocess.call([PATH_TO_NOTEPAD_EXE, path_to_file])
    
    def TemplateGenerator(self):
        pass


class PolynomialRegressionParaInfoScreen(tk.Frame):
    def __init__(self, parent, width, height):
        super(PolynomialRegressionParaInfoScreen, self).__init__()

        self.master = parent
        self.dataset_path = ''
        self.polynomial_regression_model = None

        self.grid_columnconfigure(0, weight=1)


        # FRAMES
        labels_frame = tk.Frame(self, borderwidth=2)
        labels_frame.grid(row=0, column=0)

        input_frame = tk.Frame(self, borderwidth=2)
        input_frame.grid(row=0, column=1)

        actions_frame = tk.Frame(self, borderwidth=2)
        actions_frame.grid(row=1, column=0)

        # LABELS
        selected_dataset_label = tk.Label(labels_frame, text='Dataset')
        selected_dataset_label.grid(row=0, column=0, sticky='NSEW', padx=60, pady=20)

        test_size_label = tk.Label(labels_frame, text='Test Size')
        test_size_label.grid(row=1, column=0, sticky='NSEW', padx=60, pady=20)

        graph_title_label = tk.Label(labels_frame, text='Graph Title')
        graph_title_label.grid(row=2, column=0, sticky='NSEW', padx=60, pady=20)

        x_axis_label = tk.Label(labels_frame, text='X Label')
        x_axis_label.grid(row=2, column=0, sticky='NSEW', padx=60, pady=20)
        
        y_axis_label = tk.Label(labels_frame, text='Y Label')
        y_axis_label.grid(row=3, column=0, sticky='NSEW', padx=60, pady=20)
        
        training_data_point_colour_label = tk.Label(labels_frame, text='Training Data Point Colour')
        training_data_point_colour_label.grid(row=4, column=0, sticky='NSEW', padx=60, pady=20)

        predicted_curve_colour = tk.Label(labels_frame, text='Predicted Curve Colour')
        predicted_curve_colour.grid(row=5, column=0, sticky='NSEW', padx=60, pady=20)

        to_predict_value_label = tk.Label(labels_frame, text='Predict value for')
        to_predict_value_label.grid(row=6, column=0, sticky='NSEW', padx=60, pady=20)


        # INPUTS
        self.dataset_selection_button = tk.Button(input_frame, text='Select Dataset', command=lambda: self.SelectDataset())
        self.dataset_selection_button.grid(row=0, column=1, sticky='NSEW', padx=60, pady=20)

        self.test_size_input = tk.Entry(input_frame)
        self.test_size_input.grid(row=1, column=1, sticky='NSEW', padx=60, pady=20)

        self.graph_title_input = tk.Entry(input_frame)
        self.graph_title_input.grid(row=2, column=1, sticky='NSEW', padx=60, pady=20)

        self.x_axis_label_input = tk.Entry(input_frame)
        self.x_axis_label_input.grid(row=2, column=1, sticky='NSEW', padx=60, pady=20)

        self.y_axis_label_input = tk.Entry(input_frame)
        self.y_axis_label_input.grid(row=3, column=1, sticky='NSEW', padx=60, pady=20)

        self.training_data_point_colour_input = tk.Entry(input_frame)
        self.training_data_point_colour_input.grid(row=4, column=1, sticky='NSEW', padx=60, pady=20)

        self.predicted_curve_colour_input = tk.Entry(input_frame)
        self.predicted_curve_colour_input.grid(row=5, column=1, sticky='NSEW', padx=60, pady=20)

        self.to_predict_value_input = tk.Entry(input_frame)
        self.to_predict_value_input.grid(row=6, column=1, sticky='NSEW', padx=60, pady=20)
        

        # ACTIONS
        train_button = tk.Button(labels_frame, text='Train Model', command=lambda: self.Train())
        train_button.grid(row=7, column=0, sticky='NSEW', padx=60, pady=20)

        predict_button = tk.Button(input_frame, text='Predict', command=lambda: self.Predict())
        predict_button.grid(row=7, column=1, sticky='NSEW', padx=60, pady=20)

        visualize_button = tk.Button(input_frame, text='Visualize', command=lambda: self.Visualize())
        visualize_button.grid(row=7, column=2, sticky='NSEW', padx=60, pady=20)


    def SelectDataset(self):
        self.dataset_path = filedialog.askopenfilename(initialdir="/", title="Select the Dataset", filetypes=(("CSV files","*.csv*"),("all files", "*.*")))
        dataset_path_splitted = self.dataset_path.split('/')
        dataset_name = dataset_path_splitted[-1]
        self.dataset_selection_button.config(text=dataset_name)

    def Train(self):
        self.polynomial_regression_model = PolynomialRegressionModel(dataset=self.dataset_path)
        self.polynomial_regression_model.Train(test_size=float(self.test_size_input.get()))

    def Predict(self):
        self.polynomial_regression_model.Predict()
        self.polynomial_regression_model.PredictValueFor(to_predict_value=int(self.to_predict_value_input.get()))

    def Visualize(self):
        self.polynomial_regression_model.VisualizeTrainSet(graph_title=self.graph_title_input.get(),xlabel=self.x_axis_label_input.get(),ylabel=self.y_axis_label_input.get(),train_point_colour=self.training_data_point_colour_input.get(),predicted_curve_colour=self.predicted_curve_colour_input.get())
        
        self.linear_regression_model.VisualizeTestSet(graph_title=self.graph_title_input.get(),xlabel=self.x_axis_label_input.get(),ylabel=self.y_axis_label_input.get(),train_point_colour=self.training_data_point_colour_input.get(),predicted_curve_colour=self.predicted_curve_colour_input.get())