#!flask/bin/python

# Title: Machine Learning and Statistics Project
# Author: Andrzej Kocielski, 2020; email: G00376291@gmit.ie, https://github.com/andkoc001/
# Description: Web deployment of the machine learning project. See README.md on my GitHub for more information.
# The application is based on the lecture materials, and other sources quoted as they were used in the program.
# Context: Machine Learning and Statistics, GMIT, 2021
# Lecturer: Dr. Ian McLoughlin
####################################


# # import libraries and packages
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import PolynomialFeatures

# # load the data set from file
# df_raw = pd.read_csv(r"powerproduction.txt")

# # clean the dataset by removing all observations where the power output is zero
# df = df_raw[df_raw['power'] != 0]

# # assign "speed" and "power" sets to variables X and y
# X, y = df["speed"], df["power"]

test = 17  # test wind speed value


# -------------------------------------
# Linear regression ML script
# -------------------------------------
def lin_reg(wind_speed):
    # Doc string to be added here

    # import libraries and packages
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import PolynomialFeatures

    # load the data set from file
    df_raw = pd.read_csv(r"powerproduction.txt")

    # clean the dataset by removing distorting observations
    # remove the observations where wind speed is less than 6 and the power output greated than 5 - these readings are considered affected by noise
    df = df_raw.drop(df_raw.loc[(df_raw.power > 5) & (df_raw.speed < 4)].index)
    # remove the observations where wind speed greater than 10 and power output is zero - these are considered errous readings (e.g. due to maintenance)
    df = df.drop(df.loc[(df.power == 0) & (df.speed > 10)].index)
    # remove the observations where wind power output is greater than 110 - these are considered errous readings (noise)
    df = df.drop(df.loc[(df.power > 110)].index)

    # assign "speed" and "power" sets to variables X and y
    X, y = df["speed"], df["power"]

    # random_state (seed) is set for consistancy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2020)

    # reshape the train set array
    X_train = X_train.values.reshape(-1, 1)
    y_train = y_train.values.reshape(-1, 1)
    X_test = X_test.values.reshape(-1, 1)

    # create an instance of a LinearRegression() model named lin_reg_model.
    lin_reg_model = LinearRegression()

    # Train/fit lin_reg_model on the training data.
    lin_reg_model.fit(X_train, y_train)

    # convert the the passed wind speed into an array
    # x = np.array([[wind_speed]])
    # # test.shape

    # make prediction
    result = lin_reg_model.predict([[wind_speed]])

    # convert to string
    result = str(float(result[0]))
    
    # return print(f"Simple linear regression prediction for wind speed {test}: \t{float(result):.1}")
    return result

# lin_reg(test)



# -------------------------------------
# Polynomial (5th order) regression ML script
# -------------------------------------
# Adapted from https://towardsdatascience.com/polynomial-regression-with-scikit-learn-what-you-should-know-bed9d3296f2

def poly_reg(wind_speed):
    # Doc string to be added here

    # import libraries and packages
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.pipeline import make_pipeline
    import matplotlib.pyplot as plt

    # load the data set from file
    df_raw = pd.read_csv(r"powerproduction.txt")

    # clean the dataset by removing distorting observations
    # remove the observations where wind speed is less than 6 and the power output greated than 5 - these readings are considered affected by noise
    df = df_raw.drop(df_raw.loc[(df_raw.power > 5) & (df_raw.speed < 4)].index)
    # remove the observations where wind speed greater than 10 and power output is zero - these are considered errous readings (e.g. due to maintenance)
    df = df.drop(df.loc[(df.power == 0) & (df.speed > 10)].index)
    # remove the observations where wind power output is greater than 110 - these are considered errous readings (noise)
    df = df.drop(df.loc[(df.power > 110)].index)

    # assign "speed" and "power" sets to variables X and y
    X, y = df["speed"], df["power"]

    # random_state (seed) is set for consistancy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2020)

    # reshape train set arrays
    X_train = X_train.values.reshape(-1,1)
    # print(X_train.shape)
    # print(y_train.shape)

    # create a model instance
    degree = 5 # polynomial order
    polyreg = make_pipeline(PolynomialFeatures(degree),LinearRegression())
    # train model
    polyreg.fit(X_train,y_train)

    # reshape test set
    X_test = X_test.values.reshape(-1,1)
    # print(X_test.shape)
    # print(y_test.shape)

    # make prediction for the passed wind speed
    # result = polyreg.predict(X_test)
    result = polyreg.predict([[wind_speed]]) # for a specified wind speed
    # print(f"Result: {result:.1f}")
    result = str(result[0])

    # Creating the plot
    # plt.figure()
    # plt.scatter(X_train,y_train, alpha=.2)
    # plt.plot(wind_speed,result,"rx")
    # plt.title("Polynomial regression with degree "+str(degree))
    # plt.show()
    
    # return "{:.1f}".format(result[0])

    return result
    
# poly_reg(test)


# -------------------------------------
# Random Forest ML script
# -------------------------------------
# https://www.geeksforgeeks.org/random-forest-regression-in-python/

def rand_forest(wind_speed):
    # Doc string to be added here

    # import libraries and packages
    import numpy as np
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor 
    from sklearn.model_selection import train_test_split

    # load the data set from file
    df_raw = pd.read_csv(r"powerproduction.txt")

    # clean the dataset by removing distorting observations
    # remove the observations where wind speed is less than 6 and the power output greated than 5 - these readings are considered affected by noise
    df = df_raw.drop(df_raw.loc[(df_raw.power > 5) & (df_raw.speed < 4)].index)
    # remove the observations where wind speed greater than 10 and power output is zero - these are considered errous readings (e.g. due to maintenance)
    df = df.drop(df.loc[(df.power == 0) & (df.speed > 10)].index)
    # remove the observations where wind power output is greater than 110 - these are considered errous readings (noise)
    df = df.drop(df.loc[(df.power > 110)].index)

    # assign "speed" and "power" sets to variables X and y
    X, y = df["speed"], df["power"]

    # random_state (seed) is set for consistancy
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2020)

    # reshape the train set array
    X_train = X_train.values.reshape(-1, 1)
    y_train = y_train.values
    X_test = X_test.values.reshape(-1, 1)

    # Fitting Random Forest Regression to the dataset 
    # create regressor instance 
    rand_forest_model = RandomForestRegressor(n_estimators = 100, random_state = 2020) 

    # fit the regressor with the train data subset
    rand_forest_model.fit(X_train, y_train) 
    
    # predict test set
    # test_result = rand_forest_model.predict(X_test) 
    
    # convert the the passed wind speed variable into an array
    x = np.array([[wind_speed]])
    # print(x.shape)

    # make prediction
    result = rand_forest_model.predict([[wind_speed]])

    # print(type(result))
    result = str(float(result[0]))
    # print(type(result))
    print(result)
    
    # return print(f"Random forest prediction for wind speed {test}: \t{result}")
    return result


# rand_forest(test)


# ------------------
# Check dependencies
# ------------------

# if __name__ == '__main__':
#     app.run(debug=True)
