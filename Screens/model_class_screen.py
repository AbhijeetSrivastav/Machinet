import tkinter as tk

from Core import app

from Screens import (model_class_info_screen, model_subclass_screen,
                     welcome_screen)


class ModelTypeFrame(tk.Frame):
    """Contains the model widget of side panel"""

    def __init__(self, parent, width, height):
        super(ModelTypeFrame, self).__init__()
        self.master = parent

        self.config(width=width, height=height)
        self.grid_propagate(0)

        reg = tk.Button(self, text='Regression', relief='raised', background='green', padx=3, pady=3,
                        font=('Helvetica', 10), command=lambda: self.ModelInfoDisplay('Regression'))
        reg.grid(row=0, column=0, sticky='NSEW', padx=60, pady=20)

        classi = tk.Button(self, text='Classification', relief='raised', background='green', padx=3, pady=3,
                           font=('Helvetica', 10), command=lambda: self.ModelInfoDisplay('Classification'))
        classi.grid(row=1, column=0, sticky='NSEW', padx=60, pady=20)

        clus = tk.Button(self, text='Clustering', relief='raised', background='green', padx=3, pady=3,
                         font=('Helvetica', 10), command=lambda: self.ModelInfoDisplay('Clustering'))
        clus.grid(row=2, column=0, sticky='NSEW', padx=60, pady=20)

        associate = tk.Button(self, text='Association Rule Learning', relief='raised', background='green', padx=3,
                              pady=3,
                              font=('Helvetica', 10),
                              command=lambda: self.ModelInfoDisplay('Association Rule Learning'))
        associate.grid(row=4, column=0, sticky='NSEW', padx=60, pady=20)

        reinforce = tk.Button(self, text='Reinforcment Learning', relief='raised', background='green', padx=3, pady=3,
                              font=('Helvetica', 10), command=lambda: self.ModelInfoDisplay('Reinforcment Learing'))
        reinforce.grid(row=5, column=0, sticky='NSEW', padx=60, pady=20)

        ann = tk.Button(self, text='Artifcial Neural Network', relief='raised', background='green', padx=3, pady=3,
                        font=('Helvetica', 10), command=lambda: self.ModelInfoDisplay('Artificial Neural Network'))
        ann.grid(row=6, column=0, sticky='NSEW', padx=60, pady=20)

        cnn = tk.Button(self, text='Convolutional Neural Network', relief='raised', background='green', padx=3, pady=3,
                        font=('Helvetica', 10), command=lambda: self.ModelInfoDisplay('Convolutional Neural Network'))
        cnn.grid(row=7, column=0, sticky='NSEW', padx=60, pady=20)

        dim = tk.Button(self, text='Dimensionality Reduction', relief='raised', background='green', padx=3, pady=3,
                        font=('Helvetica', 10), command=lambda: self.ModelInfoDisplay('Dimensionality Reduction'))
        dim.grid(row=8, column=0, sticky='NSEW', padx=60, pady=20)

    def ModelInfoDisplay(self, selected_model: str):
        """This method destroys the Welcome Frame and grid the selected model info frame"""
        welcome_screen.WelcomeFrame.WelcomeDestruct()
        if selected_model == "Regression":
            regression_info_frame = model_class_info_screen.RegressionInfo(parent=self, width=app.WIDTH_APP_SCREEN * 0.7,
                                                                           height=app.HEIGHT_APP_SCREEN)
            regression_info_frame.grid(row=0, column=1, sticky='e', rowspan=2)

            regression_subclass_model_frame = model_subclass_screen.RegressionModelSubTypeFrame(parent=self,
                                                                                                width=app.WIDTH_APP_SCREEN * 0.3,
                                                                                                height=app.HEIGHT_APP_SCREEN)
            regression_subclass_model_frame.grid(row=0, column=0, sticky='w', rowspan=1)

        elif selected_model == "Classification":
            classification_info_frame = model_class_info_screen.ClassificationInfo(parent=self, width=app.WIDTH_APP_SCREEN * 0.7,
                                                                                   height=app.HEIGHT_APP_SCREEN)
            classification_info_frame.grid(row=0, column=1, sticky='e', rowspan=2)

        elif selected_model == "Clustering":
            clustering_info_frame = model_class_info_screen.ClusteringInfo(parent=self, width=app.WIDTH_APP_SCREEN * 0.7,
                                                                           height=app.HEIGHT_APP_SCREEN)
            clustering_info_frame.grid(row=0, column=1, sticky='e', rowspan=2)

        elif selected_model == "Association Rule Learning":
            association_rule_learning_info_frame = model_class_info_screen.AssociationRuleLearningInfo(parent=self,
                                                                                                       width=app.WIDTH_APP_SCREEN * 0.7,
                                                                                                       height=app.HEIGHT_APP_SCREEN)
            association_rule_learning_info_frame.grid(row=0, column=1, sticky='e', rowspan=2)

        elif selected_model == "Reinforcment Learning":
            reinforcment_learning_info_frame = model_class_info_screen.ReinforcmentLearningInfo(parent=self,
                                                                                                width=app.WIDTH_APP_SCREEN * 0.7,
                                                                                                height=app.HEIGHT_APP_SCREEN)
            reinforcment_learning_info_frame.grid(row=0, column=1, sticky='e', rowspan=2)

        elif selected_model == "Artificial Neural Network":
            artificial_neural_network_info_frame = model_class_info_screen.ArtificialNeuralNetworkInfo(parent=self,
                                                                                                       width=app.WIDTH_APP_SCREEN * 0.7,
                                                                                                       height=app.HEIGHT_APP_SCREEN)
            artificial_neural_network_info_frame.grid(row=0, column=1, sticky='e', rowspan=2)

        elif selected_model == "Convolutional Neural Network":
            convolutional_neural_network_info_frame = model_class_info_screen.ConvolutionalNeuralNetworkInfo(
                parent=self, width=app.WIDTH_APP_SCREEN * 0.7,
                height=app.HEIGHT_APP_SCREEN)
            convolutional_neural_network_info_frame.grid(row=0, column=1, sticky='e', rowspan=2)

        elif selected_model == "Dimensionality Reduction":
            dimensionality_reduction_info_frame = model_class_info_screen.DimensionalityReduction(parent=self,
                                                                                                  width=app.WIDTH_APP_SCREEN * 0.7,
                                                                                                  height=app.HEIGHT_APP_SCREEN)
            dimensionality_reduction_info_frame.grid(row=0, column=1, sticky='e', rowspan=2)

    def ModelTypeFrameDestroy(self):
        self.grid_forget()
        # self.destroy()
