import pandas as pd
from sklearn.model_selection import KFold
from sklearn.utils.testing import all_estimators
import warnings
from sklearn.model_selection import cross_val_score


iris_data = pd.read_csv("data/iris.csv", encoding="utf-8")

name_id = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
y = iris_data.loc[:, "Name"].map(name_id)
x = iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]


warnings.filterwarnings('ignore')
allAlgorithms = all_estimators(type_filter="classifier")

Kfold_cv = KFold(n_splits=5, shuffle=True)

for(name, algorithm) in allAlgorithms:
    clf = algorithm()

    if hasattr(clf, "score"):
        scores = cross_val_score(clf, x, y, cv=Kfold_cv)
        print(name, "の正解率", scores)


