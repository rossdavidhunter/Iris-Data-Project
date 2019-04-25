# Ross Hunter, 2019, Iris Data Set Project

#Adapted from:https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ and https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html and 
# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

# 1. Import in all your packages

import sys
print('Python: {}'.format(sys.version))
import numpy
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import warnings
from sklearn import tree
from sklearn.metrics import accuracy_score

# 2. Import of raw data file

raw_data="iris.csv"
dataset = pandas.read_csv(raw_data)

# 3. How to view # of Rows and columns
     
print(dataset.shape)

# 4. Show first 20 rows of data, get a snapshot

print(dataset.head(20))

# 5. Obtain count, max, min and percentiles

print(dataset.describe())

# 6. Create dataset for each species

setosa=dataset[dataset['species']=='setosa']
versicolor =dataset[dataset['species']=='versicolor']
virginica =dataset[dataset['species']=='virginica']

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())

# 7. View number of rows that belong to each species

print(dataset.groupby('species').size())


# 8. Create box and whisker plots

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# 9. Create histograms

dataset.hist()
plt.show()

# 10. Create colour pie chart

labels ='setosa', 'versicolor','virginica'
colors =['red','green','yellow']
explode =(0.1,0,0)
plt.pie(dataset.groupby('species').size(),explode=explode,colors=colors,autopct='%1.1f%%', shadow=True)

# 11. Create scatter plot matrix

scatter_matrix(dataset)
plt.show()

# 12. Plotting Petal Length vs Petal Width & Sepal Length vs Sepal width

plt.figure()
fig,ax=plt.subplots(1,2,figsize=(17, 9))
dataset.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
dataset.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()

plt.show()

 



