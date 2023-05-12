# First ML Application

Although, I have made some simple single layer linear regression and logistic regression models, this is the first machine learning based application I made.

This application uses Pytorch as the machine learning framework

## Using the application
After cloning the repository and navigating to the directory,

If you're using raw python,
```
$ python -m venv <environment_name>
$ <environment_name>\Scripts\activate.bat
$ pip install -r requirements.txt
```

or if you are using anaconda,

```
$ conda env create -f environment.yml
$ conda activate <environment_name>
```

## `Starting the app`:

```
$ python app.py
```

## Dataset

The dataset used is [MNIST dataset](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv). 

## About the model

The model has:
- `784` nodes in input layer
- `100` nodes in hidden layer
- `10` nodes in output layer

The model uses:
- `ReLU` Activation for the hidden layer
- `softmax` Activation for the output layer
- `Cross Entropy` Loss function

The model is trained with:
- `Learning Rate = 0.05`
- `Epochs = 1500`