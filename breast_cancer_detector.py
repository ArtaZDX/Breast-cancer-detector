from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = load_breast_cancer()

x = data['data']
y = data['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

clf = KNeighborsClassifier()
clf.fit(x_train, y_train)

print(clf.score(x_test, y_test))
print(len(data['feature_names']))

column_data = np.concatenate([data['data'], data['target'][:, None]], axis=1)
column_names = np.concatenate([data['feature_names'], ["class"]])

df = pd.DataFrame(column_data, columns=column_names)

print(df.corr())

sns.heatmap(df.corr(), cmap="coolwarm", annot=True, annot_kws={"fontsize": 8})
plt.tight_layout()
plt.show()
