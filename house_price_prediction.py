# -*- coding: utf-8 -*-
"""House Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XNM-dlBLRKiitW67ZcBIcA6j1AzEuQwI

Importing the Dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

"""Importing the California Price Dataset"""

house_price_dataset = sklearn.datasets.fetch_california_housing()

house_price_dataset

#loading the dataset to a pandas dataframe
house_price_dataframe = pd.DataFrame(house_price_dataset.data, columns = house_price_dataset.feature_names)

house_price_dataframe.head()

#add the target (house price) column to the dataframe
house_price_dataframe['price'] = house_price_dataset.target

house_price_dataframe.head()

#checking the number of rows and columns in the dataframe
house_price_dataframe.shape

#check for missing values
house_price_dataframe.isnull().sum()

#statistical measures of the dataset
house_price_dataframe.describe()

#Understanding the correlation between various features in the dataset
#There're two types of correlations, 1. positive 2. negative

#1. Positive = if one variable increases then other variable increases
#2. Negative = if one variable decreases then other also decreases.

correlation = house_price_dataframe.corr()

#constructing a heatmap to understand the correlation ( is very important in understanding the relation between various rows and columns.)
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt= '.1f', annot = True, annot_kws={'size':8}, cmap='Blues')

#splitting the data and target

X= house_price_dataframe.drop(['price'], axis = 1)
Y = house_price_dataframe['price']

X
Y

#splitting the data into training data and test data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 2)

print(X.shape, X_train.shape, X_test.shape)

#Model Training
# we're using XGBoost Regressor

#loading the model
model = XGBRegressor()

#training the model with X_train
model.fit(X_train, Y_train)

#Evaluation

#prediction on training data

#accuracy for prediction on training data

training_data_prediction = model.predict(X_train)

print(training_data_prediction)

# R square error
score_1 = metrics.r2_score(Y_train, training_data_prediction)

# mean abs error
score_2 = metrics.mean_absolute_error(Y_train, training_data_prediction)

print(" R squared error : ", score_1)
print(" Mean Absolute error ", score_2)

"""Visualizing the actual prices and predicted prices"""

plt.scatter(Y_train, training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Price vs Predicted Prices")
plt.show()

#prediction on training data

#accuracy for prediction on training data

testing_data_prediction = model.predict(X_test)

print(testing_data_prediction)

# R square error
score_3 = metrics.r2_score(Y_test, testing_data_prediction)

# mean abs error
score_4 = metrics.mean_absolute_error(Y_test, testing_data_prediction)

print(" R squared error : ", score_3)
print(" Mean Absolute error ", score_4)

plt.scatter(Y_test, testing_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Price vs Predicted Prices")
plt.show()

