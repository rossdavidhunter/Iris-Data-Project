# Ross Hunter, 2019, Iris Data Set Project

This repository contains my project in regards to review of Fisher's Iris Data Set as part of programming and scripting module for Higher Diploma in Data Analytics, GMIT.
[See here for instructions](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)


# Introduction

![](Iris-image.PNG)




The Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".


# What is the data set used for

The Iris flower data set is a classic, well-known data set example for data mining and data exploration. The data set contains 150 records of three different types (classes) of iris flowers with numeric values for petal length and width and sepal length and width.

This data set is traditionally used for classification and prediction. The values for length and width can be used to classify an iris into one of three iris types: Iris setosa, Iris versicolor, or Iris virginica. Visually exploring this data also lets you see the grouping (clustering) of the records into these three different types of irises.

# Who is Ronald Fisher

![](RF.PNG)






Although Ronald Fisher’s name is less well-known than some others, he was one of the twentieth century’s greatest scientists.

In addition to being probably the greatest statistician ever, he also invented experimental design and was one of the principal founders of population genetics.The importance of his book Statistical Methods for Research Workers in quantitative biology has been likened to that of Isaac Newton’s Principia in physics.



# Review of Code

1. The first step taken was to import all your packages to be able to perform your data analysis on the iris data set. Packages were imported using numpy, pandas, Mathploltlib, warnings, seaborn and sklearn. 

2. The first analysis step performed was to import the raw daw. I downloaded file to my pc and file could be read using pandas.read_csv.




![](Capture18.PNG)




3. The number of rows and columns was then obtained from raw data set. Result was 150 rows and 5 columns of sepal lenght and width, petal lenght and width and species.





![](Capture1.PNG)




4. The next analysis is to show how you can get just a quick snapshot of the data. Result shows the first 20 rows of data.




![](Capture19.PNG)





5. Then a breakdown of each attribute is performed across the 150 rows of data resulting in outputs of count, mean, standard deviation, min, max and some percentiles.




![](Capture2.PNG)




6.  Datasets were created for each species which contained 50 of setosa, versicolor and virginicia resulting in outputs of count, mean, standard deviation, min, max and some percentiles.




![](Capture20.PNG)




7. Performed a simple analysis on the the # of rows for each species.



![](Capture4.PNG)




8. Create box and whisker plots using data. This gives a clear picture of the distribution of input attributes.





![](Capture5.PNG)









9. Create Histogram. Data shows that the distribution of the petal length, when viewing all species together, has a wide distribution. It can be seen that sepal width follows a Gaussian distribution. 




![](Capture9.PNG)




10. Create simple colour pie chart. Performs a % breakdown of each species.




![](Capture11.PNG)




11. Create scatter plot matrix.Scatter plots can be useful in indicating structured relationships within the data. Its also states that diagonal grouping, i.e. linear trends, suggest high correlation and predictable relationships. 




![](Capture10.PNG)




12. Plotting Petal Length vs Petal Width & Sepal Length vs Sepal width. We can see for petal width that some petals are considerably smaller sitting between 0.0 - 0.5.




![](Capture12.PNG)





# Discussion of simple machine learning example 

This is showing application of a simple machine learning excercise with data downloaded from sklearn.

Machine learning provides capability to learn patterns from data and use experience to make predictions without the need for human intervention.

The object of this excercise is to predict the specises of flowers based of the following chaateristics:

        1. Petal Width
        2. Petal Height
        3. Sepal Width
        4. Sepal Height

The first step is to get some charateristics of the iris data set. An array list list is kept in the .data key.




![](Capture13.PNG)




In the digits.target this provides visibility on what we intend to learn.




![](Capture21.PNG)




An array of data and labels is obtained from iris.data and iris.target. 
Labels: Setosa = 0, Versicolor = 1, Virginica = 2. 

iris.target_names will give an array of names of labels



![](Capture22.PNG)                      ![](Capture23.PNG)                     



A box plot can be used to show how the data is scattered over a plane. 




![](Capture16.PNG)

0 is Sepal lenght, 1 is sepal width, 2 is petal lenght, 3 is petal width


# Training and Testing of Data

An algorithm is used for training a prediction model. The data is split out into 2 sets:

        1. Training Set 
        2. Testing Set

By training and testing on 2 diffrent sets helps ensure the algorithm identifies patterns in the data set which in turn will improve accuracy. The last 15 sets will be kept for testing and used for prediction. And the remainder the training set will be used to train the algorithm. Because the data is split out, we will get different results everytime we run the code.

# Results

On the first line you can see the outputs of labels based on the predictions.



![](Capture24.PNG)




On the second line will give you the output of the actual species.



![](Capture25.PNG)




On the last line, this will give you % accuracy. In this case it is 93.3% which is very accurate.




![](Capture26.PNG)




# References/Links
[Machine Learning Project in Python](https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
[Scikit Learn](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)
[Python - Iris Data Visulization and Explanation](https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation)
[A simple machine learning project](https://dev.to/liveedutv/a-simple-machine-learning-project-in-python-5d11)
[Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher)
[Famous Scientists](https://www.famousscientists.org/ronald-fisher/)
[Gaussian Distribution Function](http://hyperphysics.phy-astr.gsu.edu/hbase/Math/gaufcn.html)
[Anaconda](https://www.anaconda.com/)
[cmder](http://cmder.net/)
[Visual Studio Code](https://code.visualstudio.com/)


# Some useful links to videos
[Getting started in Scikit Learn with Iris Data Set](https://www.youtube.com/watch?v=hd1W4CyPX58)