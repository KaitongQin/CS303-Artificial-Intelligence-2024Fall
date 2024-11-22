from typing import List

import numpy as np
import pickle
import os

class Selector:
    def __init__(self):
        root_path = os.path.dirname(os.path.abspath(__file__))
        self.mask_code = pickle.load(open(os.path.join(root_path, 'mask_code.pkl'), 'rb'))

    def get_mask_code(self) -> List[int]:
        """
        Returns: The indices of the 30 features.
        """
        return self.mask_code
