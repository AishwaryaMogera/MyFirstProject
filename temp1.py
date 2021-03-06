    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print ("Hello World")

# importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# Importing the data set
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#taking care of the miss ng data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])