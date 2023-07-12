from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris, load_wine
import numpy as np
import matplotlib.pyplot as plt

irisData = load_iris()
wineData = load_wine()

X_iris = irisData.data
y_iris = irisData.target

X_wine = wineData.data
y_wine = wineData.target

X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
    X_iris, y_iris, test_size=0.2, random_state=42)

X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(
    X_wine, y_wine, test_size=0.2, random_state=42)

neighbors = np.arange(1, 9)
train_accuracy_iris = np.empty(len(neighbors))
test_accuracy_iris = np.empty(len(neighbors))
train_accuracy_wine = np.empty(len(neighbors))
test_accuracy_wine = np.empty(len(neighbors))

for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_iris, y_train_iris)

    train_accuracy_iris[i] = knn.score(X_train_iris, y_train_iris)
    test_accuracy_iris[i] = knn.score(X_test_iris, y_test_iris)

for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_wine, y_train_wine)

    train_accuracy_wine[i] = knn.score(X_train_wine, y_train_wine)
    test_accuracy_wine[i] = knn.score(X_test_wine, y_test_wine)

fig, ax = plt.subplots(2)

ax[0].plot(neighbors, test_accuracy_iris,
           label='Iris testing dataset accuracy')
ax[0].plot(neighbors, train_accuracy_iris,
           label='Iris training dataset accuracy')
ax[0].set_xlabel('n_neighbors')
ax[0].set_ylabel('Accuracy')
ax[0].legend()

ax[1].plot(neighbors, test_accuracy_wine,
           label='Wine testing dataset accuracy')
ax[1].plot(neighbors, train_accuracy_wine,
           label='Wine training dataset accuracy')
ax[1].set_xlabel('n_neighbors')
ax[1].set_ylabel('Accuracy')
ax[1].legend()

plt.show()
