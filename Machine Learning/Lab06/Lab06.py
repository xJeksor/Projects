from sklearn import svm, tree, datasets, model_selection
import pandas as pd

iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target

param_grid = [
    {'C': [0.1, 1, 10], 'kernel': ['linear']},
    {'C': [0.1, 1, 10], 'gamma': [0.1, 0.01], 'kernel': ['rbf']},
    {'C': [0.1, 1, 10], 'degree': [2, 3, 4], 'kernel': ['poly']}
]

best_accuracy = 0
best_n = 0

for n in (2, 10):

    clf_svm = svm.SVC(kernel='poly', degree=n)

    scores = model_selection.cross_val_score(clf_svm, X, y, cv=5)

    accuracy = scores.mean()

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_n = n

clf_svm = svm.SVC(kernel='poly', degree=best_n, C=1)
clf_svm.fit(X, y)

new_data = [[5.0, 3.0], [4.5, 2.0]]
print("Najlepszy klasyfikator dla n={}: {}".format(best_n, clf_svm))
print("Klasyfikacja nowych danych:", clf_svm.predict(new_data))
