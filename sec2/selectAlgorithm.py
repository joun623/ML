import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
from sklearn.utils.testing import all_estimators

iris_data = pd.read_csv("data/iris.csv", encoding="utf-8")

name_id = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
y = iris_data.loc[:, "Name"].map(name_id)
x = iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]

print(y)

x_train, x_test, y_train, y_test =  train_test_split(x, y, test_size = 0.2,
        train_size = 0.8, shuffle = True)

warnings.filterwarnings('ignore')
allAlgorithms = all_estimators(type_filter="classifier")

for(name, algorithm) in allAlgorithms:
    clf = algorithm()

    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    print(name, "の正解率", accuracy_score(y_test, y_pred))


