#!flask/bin/python

# Title: Machine Learning and Statistics Project
# Author: Andrzej Kocielski, 2020; email: G00376291@gmit.ie, https://github.com/andkoc001/
# Description: Web deployment of the machine learning project. See README.md on my GitHub for more information.
# The application is based on the lecture materials, and other sources quoted as they were used in the program.
# Context: Machine Learning and Statistics, GMIT, 2020
# Lecturer: Dr. Ian McLoughlin
####################################


# -------------------------------------
# Import external modules and databases
# -------------------------------------

# flask for web app.
import flask as fl
# numpy for numerical work.
import numpy as np
# import Python functions from another file
from wind_power import poly_reg
from wind_power import lin_reg
from wind_power import rand_forest


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt


# Create a new web app instance
app = fl.Flask(__name__)


# -----------
# Flask routs
# -----------

# Add root route.
@app.route("/")
def home():
    return app.send_static_file('index.html')

# Predict the power output based on wind speed
@app.route('/api/lin-reg-model/<int:wind>')
def lin_r(wind):
    # return "wind" 
    result = lin_reg(wind)
    # return {"value": str([result])}
    return result

# Predict the power output based on wind speed
@app.route('/api/poly-reg-model/<int:wind>')
def poly_r(wind):
    result = poly_reg(wind)
    # return {"value": str([result])}
    return result

# Predict the power output based on wind speed
@app.route('/api/rand-forest-model/<int:wind>')
def rand_f(wind):
    result = rand_forest(wind)
    # return {"value": str([result])}
    return result


# Add uniform route.
@app.route('/api/uniform')
def uniform():
    return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal():
    return {"value": np.random.normal()}

# ------------------
# Check dependencies
# ------------------

if __name__ == '__main__':
    app.run(debug=True)
