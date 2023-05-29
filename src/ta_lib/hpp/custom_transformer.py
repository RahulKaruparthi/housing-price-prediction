import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

# rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    """Combined Attributes Adder Class"""
    def __init__(self,indices):
        # self.rooms_ix = 3
        # self.bedrooms_ix = 4
        # self.population_ix = 5
        # self.households_ix = 6

        self.indices = indices
        self.rooms_ix = self.indices[0]
        self.bedrooms_ix = self.indices[1]
        self.population_ix = self.indices[2]
        self.households_ix = self.indices[3]


    def fit(self, y=None):
        return self

    def transform(self, x):
        """
        Returns the attributes added numpy array of dataset provided.

        Parameters
        ----------
            X: np.array dataset.

        Returns
        ------- 
            data_frame with added attributes: np.array.
        """
        rooms_per_household = x[:, self.rooms_ix] / x[:, self.households_ix]
        population_per_household = x[:, self.population_ix] / x[:, self.households_ix]
        bedrooms_per_room = x[:, self.bedrooms_ix] / x[:, self.rooms_ix]

        print('ok')

        return np.c_[x, rooms_per_household, population_per_household, bedrooms_per_room]

    def inverse_transform(self,x):
        """
        Returns the original dataframe of a transformed dataframe.

        Parameters
        ----------
            X: np.array transformed dataset.

        Returns
        ------- 
            data_frame original: np.array.
        """

        if x.shape[1] > 10:
            x = np.delete(x,[10,11,12],1)
        
        return x