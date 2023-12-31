import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV

iris_data = pd.read_csv("data/iris.csv", encoding="utf-8")

y = iris_data.loc[:, "Name"]
x = iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]

x_train, x_test, y_train, y_test =  train_test_split(x, y, test_size = 0.2,
    train_size = 0.8, shuffle = True)

parameters = [
        {"C": [1, 10, 100, 1000], "kernel": ["linear"]},
        {"C": [1, 10, 100, 1000], "kernel": ["rbf"], "gamma": [0.001, 0.0001]},
        {"C": [1, 10, 100, 1000], "kernel": ["sigmoid"], "gamma": [0.001, 0.00001]}
]


kfold_cv = KFold(n_splits=5, shuffle=True)
clf = GridSearchCV( SVC(), parameters, cv= kfold_cv)

clf.fit(x_train, y_train)

print("最適なパラメタ", clf.best_estimator_)

y_pred = clf.predict(x_test)
print("評価時の正解率 = ", accuracy_score(y_test, y_pred))
