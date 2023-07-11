import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


def count_codePoint(str):
    counter = np.zeros(65535)

    for i in range(len(str)):
        code_point = ord(str[i])
        if code_point > 65535:
            continue
        counter[code_point] += 1

    counter = counter / len(str)
    return counter

ja_str = 'これは日本語の文章です。'
en_str = 'This is English Sentences.'

x_train = [count_codePoint(ja_str), count_codePoint(en_str)]
y_train = ['ja', 'en']

clf = GaussianNB()
clf.fit(x_train, y_train)

ja_test_str = 'こんにちは'
en_test_str = 'Hello'


x_test = [count_codePoint(en_test_str), count_codePoint(ja_test_str)]
y_test = ['en', 'ja']

y_pred = clf.predict(x_test)
print(y_pred)
print("正解率 = ", accuracy_score(y_test, y_pred))
