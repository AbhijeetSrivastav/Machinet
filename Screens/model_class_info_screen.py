import tkinter as tk
from tkinter import ttk


class ModelClassInfoSchema(tk.Frame):
    """General Info Screen Schema class"""

    def __init__(self):
        super(ModelClassInfoSchema, self).__init__()


class RegressionInfo(ModelClassInfoSchema):
    def __init__(self, parent, width, height):
        super(RegressionInfo, self).__init__()

        self.master = parent

        self.config(border=5, bg='black', width=width, height=height)

        test_label = ttk.Label(self, text='Regression', anchor='center')
        test_label.grid(row=0, column=0)


class ClassificationInfo(ModelClassInfoSchema):
    def __init__(self, parent, width, height):
        super(ClassificationInfo, self).__init__()

        test_label = ttk.Label(self, text='Classification')
        test_label.grid(row=0, column=0)


class ClusteringInfo(ModelClassInfoSchema):
    def __init__(self, parent, width, height):
        super(ClusteringInfo, self).__init__()

        test_label = ttk.Label(self, text='Classification')
        test_label.grid(row=0, column=0)


class AssociationRuleLearningInfo(ModelClassInfoSchema):
    def __init__(self, parent, width, height):
        super(AssociationRuleLearningInfo, self).__init__()

        test_label = ttk.Label(self, text='Classification')
        test_label.grid(row=0, column=0)


class ReinforcmentLearningInfo(ModelClassInfoSchema):
    def __init__(self, parent, width, height):
        super(ReinforcmentLearningInfo, self).__init__()

        test_label = ttk.Label(self, text='Classification')
        test_label.grid(row=0, column=0)


class ArtificialNeuralNetworkInfo(ModelClassInfoSchema):
    def __init__(self, parent, width, height):
        super(ArtificialNeuralNetworkInfo, self).__init__()

        test_label = ttk.Label(self, text='Classification')
        test_label.grid(row=0, column=0)


class ConvolutionalNeuralNetworkInfo(ModelClassInfoSchema):
    def __init__(self, parent, width, height):
        super(ConvolutionalNeuralNetworkInfo, self).__init__()

        test_label = ttk.Label(self, text='Classification')
        test_label.grid(row=0, column=0)


class DimensionalityReduction(ModelClassInfoSchema):
    def __init__(self, parent, width, height):
        super(DimensionalityReduction, self).__init__()

        test_label = ttk.Label(self, text='Classification')
        test_label.grid(row=0, column=0)

    # @staticmethod
    # def DestructInfoFrame():
    #     RegressionInfo.grid_forget(self)
