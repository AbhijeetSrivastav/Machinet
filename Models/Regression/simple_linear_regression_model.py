"""Simple Linear Regression Model"""
from calendar import c
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class LinearRegressionModel:
    def __init__(self, dataset, input_vector_begin_index=0, input_vector_end_index=-1, target_vector_index=-1):
        super(LinearRegressionModel, self).__init__()
        pass

        # Importing Datasets

        dataset = pd.read_csv(dataset)
        self.X = dataset.iloc[:, input_vector_begin_index:input_vector_end_index].values
        self.Y = dataset.iloc[:, target_vector_index].values

    def Train(self, test_size):
        # Splitting the Dataset into Training and Test Set
        global X_train, X_test, Y_train, Y_test

        X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, test_size=test_size, random_state=0)

        # Training the model
        global regressor
        regressor = LinearRegression()
        regressor.fit(X_train, Y_train)

    def Predict(self):
        # Predicting the Test Result
        y_pred = regressor.predict(X_test)
        return y_pred

    def VisualizeTrainSet(self, graph_title, xlabel, ylabel, train_point_colour, predicted_curve_colour):
        # Visualizing the Training Set Result

        train_plot = plt
        train_plot.scatter(X_train, Y_train, c=train_point_colour)
        train_plot.plot(X_train, regressor.predict(X_train), color=predicted_curve_colour)
        train_plot.title('Training Set' + '--' + graph_title)
        train_plot.xlabel(xlabel)
        train_plot.ylabel(ylabel)
        train_plot.show()

    def VisualizeTestSet(self, graph_title, xlabel, ylabel, train_point_colour, predicted_curve_colour):
        # Visualizing the Test Set Result
        test_plot = plt
        test_plot.scatter(X_test, Y_test, color=train_point_colour)
        test_plot.plot(X_train, regressor.predict(X_train), color=predicted_curve_colour)
        test_plot.title('Test Set' + '--' + graph_title)
        test_plot.xlabel(xlabel)
        test_plot.ylabel(ylabel)
        test_plot.show()

    def PredictValueFor(self, to_predict_value):
        # Making a single prediction
        # print(regressor.predict([[to_predict_value]]))
        # print(regressor.coef_)
        # print(regressor.intercept_)
        predicted_values = [regressor.predict([[to_predict_value]]), regressor.coef_, regressor.intercept_]
        return predicted_values
