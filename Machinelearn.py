from sklearn import datasets
import seaborn as sns
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Simple Machine Learning Example using data from sklearn

# Verbatim: https://dev.to/liveedutv/a-simple-machine-learning-project-in-python-5d11

iris = datasets.load_iris()
digits = datasets.load_digits()
print(digits.data)
print(digits.target)
print(iris.data)
print(iris.target)
print(iris.target_names)

# Shows array of the data
iris_data = iris.data 

# Shows array of the labels
iris_target = iris.target 

# Create a Box Plot of data
sns.boxplot(data = iris_data,width=0.5,fliersize=5)
sns.set(rc={'figure.figsize':(1,10)})

plt.show()

# Randomly splits the data set
iris_test_ids = np.random.permutation(len(iris_data)) 

# Splits data and leaves last 15 entries for testing, remainder for training
iris_train_one = iris_data[iris_test_ids[:-15]]
iris_test_one = iris_data[iris_test_ids[-15:]]
iris_train_two = iris_target[iris_test_ids[:-15]]
iris_test_two = iris_target[iris_test_ids[-15:]]

# Uses the decision tree for classification
iris_classify = tree.DecisionTreeClassifier()

# Training or fitting the classifier using the training set
iris_classify.fit(iris_train_one, iris_train_two) 

# Makes predictions on the test dataset
iris_predict = iris_classify.predict(iris_test_one) 

 # Labels predicted species
print(iris_predict) 

# Actual labels
print (iris_test_two) 

# % accuracy metric
print (accuracy_score(iris_predict, iris_test_two)*100) 

