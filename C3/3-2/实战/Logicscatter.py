from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np


iris = load_iris()
data = iris.data
target = iris.target
X = data[0:100, [0, 2]]
y = target[0:100]
label = np.array(y)

# 标签0：Setosa，标签1：Versicolor
index_0 = np.where(label == 0)
plt.scatter(X[index_0, 0], X[index_0, 1], marker='x', color='b', label='0', s=15)
index_1 = np.where(label == 1)
plt.scatter(X[index_1, 0], X[index_1, 1], marker='o', color='r', label='1', s=15)
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend(loc='upper left')
plt.show()
