import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.datasets import load_wine

data = load_wine()
x, y = data.data, data.target

