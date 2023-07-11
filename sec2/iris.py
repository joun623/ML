import pandas as pd
# train:test split
from sklearn.model_selection import train_test_split
# svm: support vector machine
# svc: support vector machine classification
from sklearn.svm import SVC
# metrix
from sklearn.metrics import accuracy_score

iris_data = pd.read_csv("data/iris.csv", encoding="utf-8")

y = iris_data.loc[:, "Name"]
x = iris_data.loc[:, ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]

x_train, x_test, y_train, y_test = train_test_split(x, y,
        test_size=0.2, train_size = 0.8, shuffle = True)

clf = SVC()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)
print("正解率 = ", accuracy_score(y_test, y_pred))
