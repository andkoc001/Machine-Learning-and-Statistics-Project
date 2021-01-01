#!flask/bin/python

# Title: Machine Learning and Statistics Project
# Author: Andrzej Kocielski, 2020; email: G00376291@gmit.ie, https://github.com/andkoc001/
# Description: Web deployment of the machine learning project. See README.md on my GitHub for more information.
# The application is based on the lecture materials, and other sources quoted as they were used in the program.
# Context: Machine Learning and Statistics, GMIT, 2020
# Lecturer: Dr. Ian McLoughlin
####################################

from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
test = 15  # test wind speed value

# -------------------------------------
# Polynomial (7th order) regression ML script
# -------------------------------------

# import libraries and packages


def poly_reg(wind_speed):

    # load the data set from file
    df_raw = pd.read_csv(r"../powerproduction.txt")

    # clean the dataset by removing all observations where the power output is zero
    df = df_raw[df_raw['power'] != 0]

    # create a shorthand for the column names
    X = df.iloc[:, 0].values.reshape(-1, 1)
    y = df.iloc[:, 1]

    # develop a regression model
    poly = PolynomialFeatures(degree=7)  # 7th polynomial order
    X_poly = poly.fit_transform(X)

    # ask our model to fit the data.
    poly_reg = LinearRegression().fit(X_poly, y)

    # perform regression to predict the power output out of wind speed
    y_pred = poly_reg.predict(X_poly)

    # input wind speed for prediction
    x = np.array([[wind_speed]])
    # define prediction

    prediction = (-5.11800967e-06*pow(x, 7)) + 4.48301902e-04*pow(x, 6) - 1.52309426e-02*pow(x, 5) + 2.50368085e-01 * \
        pow(x, 4) - 2.04365136e+00*pow(x, 3) + 8.13376871e+00 * \
        pow(x, 2) - 1.38470256e+01*pow(x, 1) + 10.91407191*pow(x, 0)

    return print(float(prediction))


poly_reg(test)


# -------------------------------------
# Linear regression ML script
# -------------------------------------

def lin_reg(wind_speed):
    '''
    Doc string to be added here
    '''

    # load the data set from file
    df_raw = pd.read_csv(r"../powerproduction.txt")

    # clean the dataset by removing all observations where the power output is zero
    df = df_raw[df_raw['power'] != 0]

    # assign "speed" and "power" sets to variables X and y
    X, y = df["speed"], df["power"]

    # random_state (seed) is set for consistancy
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=2020)

    # convert the array shape and unify the lengths
    X_train = X_train.values.reshape(-1, 1)
    y_train = y_train.values.reshape(-1, 1)
    X_test = X_test.values.reshape(-1, 1)

    # create an instance of a LinearRegression() model named lin_reg_model.
    lin_reg_model = LinearRegression()

    # Train/fit lin_reg_model on the training data.
    lin_reg_model.fit(X_train, y_train)

    # input wind speed for prediction
    test = np.array([[wind_speed]])
    # test.shape

    # define prediction
    # prediction = lin_reg_model.predict(X_test).values.reshape(-1,1)
    prediction = lin_reg_model.predict(test)

    return print(float(prediction))


lin_reg(test)
# ------------------
# Check dependencies
# ------------------

# if __name__ == '__main__':
#     app.run(debug=True)
