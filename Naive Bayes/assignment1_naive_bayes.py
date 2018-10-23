
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os
import pandas as pd

os.chdir(r'g:\\Programs\\python\\Machine Learning\\Datasets')

data = pd.read_csv("heartdisease-train.csv")
test_set = pd.read_csv("heartdisease-test.csv")
# X = np.array(data.loc[:, data.columns[:-1]])
# Y = np.array(data.loc[:, data.columns[-1:]])
X = data.loc[:, data.columns[:-1]]
Y = data.loc[:, data.columns[-1:]]
scaled_X = MinMaxScaler().fit_transform(X)
# scaled_Y = MinMaxScaler().fit_transform(Y)

# MODELS
gnb = GaussianNB()

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X, Y.values.ravel())
y_pred = knn.predict(test_set.loc[:, test_set.columns[:-1]])
score0 = accuracy_score(test_set.loc[:, test_set.columns[-1:]], y_pred)
print("KNN Accuracy: {}%".format(score0 * 100))

knn.fit(scaled_X, Y.values.ravel())
y_pred = knn.predict(test_set.loc[:, test_set.columns[:-1]])
score0 = accuracy_score(test_set.loc[:, test_set.columns[-1:]], y_pred)
print("KNN Accuracy(Scaled Value): {}%".format(score0 * 100))

y_pred = gnb.fit(X, Y.values.ravel()).predict( test_set.loc[:, test_set.columns[:-1]] )
score1 = accuracy_score(test_set.loc[:, test_set.columns[-1:]], y_pred)
print("Gaussian Accuracy: {}%".format(score1 * 100))

y_pred = gnb.fit(scaled_X, Y.values.ravel()).predict( test_set.loc[:, test_set.columns[:-1]] )
score1 = accuracy_score(test_set.loc[:, test_set.columns[-1:]], y_pred)
print("Gaussian Accuracy(Scaled value): {}%".format(score1 * 100))