# Machine Learning and Statistics - Project

Machine Learning and Statistics module, Data Analytics Course, GMIT 2020-2021  
Lecturer: Dr. Ian McLoughlin

>Author: **Andrzej Kocielski**  
>Github: [andkoc001](https://github.com/andkoc001/)  
>Email: G00376291@gmit.ie

___

## Introduction

This repository houses my assignment project for the Machine Learning and Statistics module, Galway-Mayo Institute of Technology, 2020.

### Project objectives

The objective of the project is to develop a web service to make predictions using Machine Learning (ML) paradigm.

The goal of the project is to produce a model or models that, based on the provided dataset _power production_, and through applying the appropriate ML techniques, predict power output generated by wind turbine from the wind. The power output predictions should be generated in response to wind speed values to be obtained as HTTP requests.

The detailed project instruction can be found in the pdf [file](https://github.com/andkoc001/Machine-Learning-and-Statistics-Project/blob/main/assessment.pdf).

### Assignment delivery

The project is about development of a machine learning models in Jupyter Notebook environment, using existing algorithms and tools, such as Keras, TensorFlow or Scikit learn packages. The applied models are subsequently assesst on their accuracy.

In the Jupyter Notebook [Powerproduction_ML.ipynb](https://github.com/andkoc001/data_synthesis/blob/master/Powerproduction_ML.ipynb), I have incorporated the research and described the project progress. It is illustrated the machine learning concepts and applied methods together with relevant code snippets. The notebook includes also the calculated outputs and plots with the accompanying descriptions.

A web app is built upon the Flask framework. The local server hosts the selected machine learning models used in the project. An attractive front-end web page has been designed to present the results in a user-friendly way. The app returns predicted values of power output, upon user input wind speed.

The web app is also available in a virtualised container on Docker platform.

___

## Accessing the Project

### Viewing Notebook

For viewing the notebook online, it is recommended to use Jupyter Notebooks viewer, [nbviewer](https://nbviewer.jupyter.org/). Paste the link to the notebook to be inspected into the provided field.

### Accessing the Web App

In order to open the web app localy, clone or download this github repository (keep the directory structure intact).

#### __Option 1) Virtual environment__

The following steps depend on the operating system.

A) __Linux__

Within the directory, create a new virtual environment, typing in the terminal
```bash
python -m venv venv
```

Activate the virtual environment:
```bash
source venv/bin/activate 
```

Install all the required libraries listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```

Start the web app using the command:

```bash
export FLASK_APP=app.py
```

To run the server program, type:
```bash
python -m flask run
```

This will activate localhost server at <http://127.0.0.1:5000/>.

To stop the server running, press `ctrl`+`c` in terminal.

In order to leave the virtual environment:
```bash
deactivate
```

B) __Windows__

Within the directory, create a new virtual environment, typing in the terminal
```bash
python -m venv venv
```

Activate the virtual environment:
```bash
\venv\Scripts\activate.bat
```

Install all the required libraries listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```

To run the server program, type:
```bash
set FLASK_APP=app.py
```

To run the server program, type
```bash
python -m flask run
```

This will activate localhost server at <http://127.0.0.1:5000/>.

To stop the server running, press `ctrl`+`c` in terminal.

In order to leave the virtual environment:
```bash
deactivate
```

#### __Option 2) Docker__

Install Docker on your computer, typing in the terminal:
```bash
pip install docker
```

To create a new docker image, inside the directory holding the repository type:
```bash
docker build . -t wind-power-app
```

Alternatively to creating a new one, pull the image from the dockerhub, using the command:
```bash
docker pull andkoc001/wind-power-app
```

In order to create and start the docker container, execute the command:
```bash
docker run -i -t -p 5000:5000 --rm wind-power-app 
```

This will activate localhost server at <http://127.0.0.1:5000/>.

To stop the server running, press `ctrl`+`c` in terminal. The container will be automaticly removed.

___

## References

General, high-level, reference sources are listed below. References to specific problems are included in the Notebook.

### Regarding the project

- Project details [project brief](https://github.com/andkoc001/Machine-Learning-and-Statistics/blob/main/assessment.pdf).

### Regarding Python environment and tools

- [Python](https://docs.python.org/3/) - the programming language used for the project
- [Jupyter Notebook](https://jupyter.org/documentation) - interactive python code editor
- [NumPy](https://numpy.org/) - scientific computing with n-dimensional arrays
- [Pandas](https://pandas.pydata.org/) - data analysis and manipulation tool
- [Scikit-learn](https://scikit-learn.org/) - machine learning library
- [Matplotlib](https://matplotlib.org/) - plotting library
- [Seaborn](https://seaborn.pydata.org/) - data visualisation

### Regarding web app deployment and virtualisation

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - web development framework
- [Docker](https://www.docker.com/resources/what-container) - OS-level virtualisation platform

___

Andrzej Kocielski, October 2020 - January 2021
