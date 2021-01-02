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
from static.wind_power import poly_reg # check the names here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Create a new web app instance
app = fl.Flask(__name__)


# -----------
# Flask routs
# -----------

# Add root route.
@app.route("/")
def home():
    return app.send_static_file('index.html')

# Add uniform route.
@app.route('/api/uniform')
def uniform():
    return {"value": np.random.uniform()}

# Add normal route.
@app.route('/api/normal')
def normal():
    return {"value": np.random.normal()}

# Predict the power output based on wind speed
@app.route('/wind-power/<float:wind>')
def poly_reg(wind):

    predict = wind_power.poly_reg(wind)

    return predict

# ------------------
# Check dependencies
# ------------------

if __name__ == '__main__':
    app.run(debug=True)
