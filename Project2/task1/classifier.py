import numpy as np
import pickle
import joblib
from pathlib import Path
import os


class Classifier:
    def __init__(self):
        """
        You can load the model as a member variable while instantiation the classifier
        """
        root_path = os.path.dirname(os.path.abspath(__file__))
        self.model = pickle.load(open(Path(root_path, 'classification_model.pkl'), 'rb'))
        self.mean = pickle.load(open(Path(root_path, 'classification_mean.pkl'), 'rb'))
        self.std_dev = pickle.load(open(Path(root_path, 'classification_std.pkl'), 'rb'))
        pass

    def inference(self, X: np.array) -> np.array:
        """
        Inference a single data
        Args:
            X:  All the feature vectors with dim=256 of the data which needs to be classified, X.shape=[a, 256], a is the
                number of the test data.

        Returns:
            All classification results, is an int vector with dim=a, where a is the number of the test data. The ith
            element of the results vector is the classification result of ith test data, which is the index of the
            category.
        """
        return self.model.predict((X - self.mean) / self.std_dev)
