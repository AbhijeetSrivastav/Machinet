"""Polynomial Linear Regression Model"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

class PolynomialRegressionModel:
    def __init__(self, dataset):
        super(PolynomialRegressionModel, self).__init__()
        pass

        # Importing Datasets

        dataset = pd.read_csv(dataset)
        self.X = dataset.iloc[:, :-1].values
        self.Y = dataset.iloc[:, -1].values

    def Train(self, test_size):
        # Splitting the Dataset into Training and Test Set
        global X_train, X_test, Y_train, Y_test

        X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, test_size=test_size, random_state=0)

        # Training the model
        global poly_reg
        poly_reg = PolynomialFeatures(degree=3)
        self.X_poly = poly_reg.fit_transform(X_train)
        self.lin_reg = LinearRegression()
        self.lin_reg.fit(self.X_poly, Y_train)

    def Predict(self):
        # Predicting the Test Result
        y_pred = self.lin_reg.predict(X_test)

    def VisualizeTrainSet(self, graph_title, xlabel, ylabel, train_point_colour, predicted_curve_colour):
        # Visualizing the Training Set Result

        train_plot = plt
        train_plot.plot(X_train, self.lin_reg.predict(self.X_poly), color=predicted_curve_colour)
        train_plot.title('Training Set')
        train_plot.xlabel(xlabel)
        train_plot.ylabel(ylabel)
        train_plot.show()

    def VisualizeTestSet(self, graph_title, xlabel, ylabel, train_point_colour, predicted_curve_colour):
        # Visualizing the Test Set Result
        test_plot = plt
        test_plot.scatter(X_test, Y_test, color=train_point_colour)
        test_plot.plot(X_train, self.lin_reg.predict(X_train), color=predicted_curve_colour)
        test_plot.title('Test Set')
        test_plot.xlabel(xlabel)
        test_plot.ylabel(ylabel)
        test_plot.show()

    def PredictValueFor(self, to_predict_value):
        # Making a single prediction
        print(self.lin_reg.predict([[to_predict_value]]))
        print(self.lin_reg.coef_)
        print(self.lin_reg.intercept_)