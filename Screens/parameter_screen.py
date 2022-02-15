import tkinter as tk
from tkinter import filedialog
from Core import app
from Models.Regression.simple_linear_regression_model import LinearRegressionModel


class ParameterInfoSchema(tk.Frame):
    def __init__(self):
        super(ParameterInfoSchema, self).__init__()


class LinearRegressionParaInfoScreen(ParameterInfoSchema):
    def __init__(self, parent, width, height):
        super(LinearRegressionParaInfoScreen, self).__init__()

        self.master = parent
        self.dataset_path = ''
        self.linear_regression_model = None

        self.config(border=5, bg='black', width=app.WIDTH_APP_SCREEN, height=app.HEIGHT_APP_SCREEN)

        selected_dataset_label = tk.Label(self, text='Dataset')
        selected_dataset_label.grid(row=0, column=0, sticky='NSEW', padx=60, pady=20)

        self.dataset_selection_button = tk.Button(self, text='Select Dataset', command=lambda: self.SelectDataset())
        self.dataset_selection_button.grid(row=0, column=1, sticky='NSEW', padx=60, pady=20)

        test_size_label = tk.Label(self, text='Test Size')
        test_size_label.grid(row=1, column=0, sticky='NSEW', padx=60, pady=20)

        self.test_size_input = tk.Entry(self)
        self.test_size_input.grid(row=1, column=1, sticky='NSEW', padx=60, pady=20)

        graph_title_label = tk.Label(self, text='Graph Title')
        graph_title_label.grid(row=2, column=0, sticky='NSEW', padx=60, pady=20)

        self.graph_title_input = tk.Entry(self)
        self.graph_title_input.grid(row=2, column=1, sticky='NSEW', padx=60, pady=20)

        x_axis_label = tk.Label(self, text='X Label')
        x_axis_label.grid(row=2, column=0, sticky='NSEW', padx=60, pady=20)

        self.x_axis_label_input = tk.Entry(self)
        self.x_axis_label_input.grid(row=2, column=1, sticky='NSEW', padx=60, pady=20)

        y_axis_label = tk.Label(self, text='Y Label')
        y_axis_label.grid(row=3, column=0, sticky='NSEW', padx=60, pady=20)

        self.y_axis_label_input = tk.Entry(self)
        self.y_axis_label_input.grid(row=3, column=1, sticky='NSEW', padx=60, pady=20)

        training_data_point_colour_label = tk.Label(self, text='Training Data Point Colour')
        training_data_point_colour_label.grid(row=4, column=0, sticky='NSEW', padx=60, pady=20)

        self.training_data_point_colour_input = tk.Entry(self)
        self.training_data_point_colour_input.grid(row=4, column=1, sticky='NSEW', padx=60, pady=20)

        predicted_curve_colour = tk.Label(self, text='Predicted Curve Colour')
        predicted_curve_colour.grid(row=5, column=0, sticky='NSEW', padx=60, pady=20)

        self.predicted_curve_colour_input = tk.Entry(self)
        self.predicted_curve_colour_input.grid(row=5, column=1, sticky='NSEW', padx=60, pady=20)

        to_predict_value_label = tk.Label(self, text='Predict value for')
        to_predict_value_label.grid(row=6, column=0, sticky='NSEW', padx=60, pady=20)

        self.to_predict_value_input = tk.Entry(self)
        self.to_predict_value_input.grid(row=6, column=1, sticky='NSEW', padx=60, pady=20)

        train_button = tk.Button(self, text='Train Model', command=lambda: self.Train())
        train_button.grid(row=7, column=0, sticky='NSEW', padx=60, pady=20)

        predict_button = tk.Button(self, text='Predict', command=lambda: self.Predict())
        predict_button.grid(row=7, column=1, sticky='NSEW', padx=60, pady=20)

        visualize_button = tk.Button(self, text='Visualize', command=lambda: self.Visualize())
        visualize_button.grid(row=7, column=2, sticky='NSEW', padx=60, pady=20)

    def SelectDataset(self):
        self.dataset_path = filedialog.askopenfilename(initialdir="/",
                                                       title="Select the Dataset",
                                                       filetypes=(("CSV files",
                                                                   "*.csv*"),
                                                                  ("all files",
                                                                   "*.*")))
        dataset_path_splited = self.dataset_path.split('/')
        dataset_name = dataset_path_splited[-1]
        self.dataset_selection_button.config(text=dataset_name)

    def Train(self):
        self.linear_regression_model = LinearRegressionModel(dataset=self.dataset_path)
        self.linear_regression_model.Train(test_size=float(self.test_size_input.get()))

    def Predict(self):
        self.linear_regression_model.Predict()
        self.linear_regression_model.PredictValueFor(to_predict_value=int(self.to_predict_value_input.get()))

    def Visualize(self):
        self.linear_regression_model.VisualizeTrainSet(graph_title=self.graph_title_input.get(),
                                                       xlabel=self.x_axis_label_input.get(),
                                                       ylabel=self.y_axis_label_input.get(),
                                                       train_point_colour=self.training_data_point_colour_input.get(),
                                                       predicted_curve_colour=self.predicted_curve_colour_input.get())
        self.linear_regression_model.VisualizeTestSet(graph_title=self.graph_title_input.get(),
                                                      xlabel=self.x_axis_label_input.get(),
                                                      ylabel=self.y_axis_label_input.get(),
                                                      train_point_colour=self.training_data_point_colour_input.get(),
                                                      predicted_curve_colour=self.predicted_curve_colour_input.get())
