import numpy as np
 import pandas as pd
 from sklearn.datasets import load_iris
 from sklearn.model_selection import train_test_split, GridSearchCV
 from sklearn.tree import DecisionTreeClassifier
 from sklearn.metrics import accuracy_score, classification_report,
 confusion_matrix
 iris = load_iris()
 X = iris.data
 y = iris.target
 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
 random_state=42)
 dt_classifier = DecisionTreeClassifier(random_state=42)
 dt_classifier.fit(X_train, y_train)
 param_grid = {
 'criterion': ['gini', 'entropy'],
 'max_depth': [None, 10, 20, 30],
 'min_samples_split': [2, 10, 20],
 'min_samples_leaf': [1, 5, 10]
 }
 grid_search = GridSearchCV(estimator=dt_classifier,
 param_grid=param_grid, cv=5, scoring='accuracy', verbose=1)
 grid_search.fit(X_train, y_train)
 print("Best Parameters:", grid_search.best_params_)
 best_dt_classifier = grid_search.best_estimator_
 y_pred = best_dt_classifier.predict(X_test)
 print("Accuracy:", accuracy_score(y_test, y_pred))
 print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
 print("Classification Report:\n", classification_report(y_test, y_pred)) 





Program:
# Importing the required packages
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
# Function to import the dataset
def importdata():
 balance_data = pd.read_csv(
 'https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data',
 sep=',', header=None
 )
 # Displaying dataset information
 print("Dataset Length: ", len(balance_data))
20
Machine learning
Dept of CSE , SNTI, Hyd
 print("Dataset Shape: ", balance_data.shape)
 print("Dataset: ", balance_data.head())
 return balance_data
# Function to split the dataset into features and target variables
def splitdataset(balance_data):
 # Separating the target variable
 X = balance_data.values[:, 1:5]
 Y = balance_data.values[:, 0]
 # Splitting the dataset into train and test
 X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)
 return X, Y, X_train, X_test, y_train, y_test
# Function to train the model using Gini index
def train_using_gini(X_train, X_test, y_train):
 # Creating the classifier object
 clf_gini = DecisionTreeClassifier(criterion="gini", max_depth=3, min_samples_leaf=5)
 # Performing training
 clf_gini.fit(X_train, y_train)
 return clf_gini
# Function to train the model using Entropy
def train_using_entropy(X_train, X_test, y_train):
 # Decision tree with entropy
 clf_entropy = DecisionTreeClassifier(
 criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5
 )
21
Machine learning
Dept of CSE , SNTI, Hyd
 # Performing training
 clf_entropy.fit(X_train, y_train)
 return clf_entropy
# Function to make predictions
def prediction(X_test, clf_object):
 y_pred = clf_object.predict(X_test)
 print("Predicted values:")
 print(y_pred)
 return y_pred
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
 print("Confusion Matrix: ", confusion_matrix(y_test, y_pred))
 print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
 print("Report : ", classification_report(y_test, y_pred))
# Function to plot the decision tree
def plot_decision_tree(clf_object, feature_names, class_names):
 plt.figure(figsize=(15, 10))
 plot_tree(clf_object, filled=True, feature_names=feature_names, class_names=class_names,
rounded=True)
 plt.show()
# Main execution
if __name__ == "__main__":
 data = importdata()
 X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
# Training using Gini Index
 clf_gini = train_using_gini(X_train, X_test, y_train)
 # Training using Entropy
22
Machine learning
Dept of CSE , SNTI, Hyd
 clf_entropy = train_using_entropy(X_train, X_test, y_train)
 # Visualizing the Decision Trees
 plot_decision_tree(clf_gini, ['X1', 'X2', 'X3', 'X4'], ['L', 'B', 'R'])
 plot_decision_tree(clf_entropy, ['X1', 'X2', 'X3', 'X4'], ['L', 'B', 'R'])
 # Operational Phase
 print("Results Using Gini Index:")
 y_pred_gini = prediction(X_test, clf_gini)
 cal_accuracy(y_test, y_pred_gini)
