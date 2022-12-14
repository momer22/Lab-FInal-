# -*- coding: utf-8 -*-
"""Lab_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lqy9hjI_9JcQTohYNZ4Z5upGX8FrgJMM
"""

# Q1: Normalize the following matrix (x) using sklearn 

from sklearn.preprocessing import Normalizer
X = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 112],
     [13, 14, 15, 16]]
transformer = Normalizer().fit(X)  # fit does nothing.
transformer
Normalizer()
transformer.transform(X)

#Q2.	Binarize matrix x by scikit learn function(s) with threshold value = 5.5
from sklearn.preprocessing import Binarizer
X = [[ 1.1, 2.2, 3.3],
     [ 4.4,  5.5,  6.6],
     [ 7.7,  8.8, 9.9]]
transformer = Binarizer().fit(X)  # fit does nothing.
transformer
Binarizer()
transformer.transform(X)

#Q3:Given the following dataset, find coefficients in 1st order linear hypothesis function 

#importing pandas module
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#Given data 
X = [[6], [8], [10], [14], [18]]
Y = [[7], [9], [13], [17.5], [18]]
X_test = [[8], [9], [11], [16], [12]]
Y_test = [[11], [8.5], [15], [18], [11]]

# creating a dictionary of data 
data = {"X":X, "Y":Y}
feature = data["X"]
Cost_func = data["Y"]

#Training and Testing
feature_train = X_test
cost_func_train = Y_test

#Obtaining model using  LinearRegression

model = LinearRegression()
model.fit(feature_train, cost_func_train)

# Obtaining model coefficients 
theta_0 = model.intercept_
theta_1 =  model.coef_[0]

print("Thetha_0 = ", theta_0)
print("Thetha_1 = ", theta_1)

#Q4: Assuming that we have a dataset with 2 features x0 and x1 as follows, 
# separate them by K-means algorithm. Notice that you make a decision about K’s value 
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler 
from matplotlib import pyplot as plt


# given data 
X0 = [[7], [5], [7], [3], [4], [1], [0], [2], [8], [6], [5], [3]]
X1 = [[5], [7], [7], [3], [6], [4], [0], [2], [7], [8], [5],[7]]
instance = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11],[12]]

data =  {"X0":X0, "X1":X1, "Instance":instance}
#graph origional  data 
from matplotlib import pyplot as plt1
plt1.scatter(X0,X1)
plt1.show()


#elbow method
wcss = []
for i in range(1,6):
    k_means = KMeans(n_clusters=i,init='k-means++', random_state=42)
    k_means.fit(X)
    wcss.append(k_means.inertia_)
#plot elbow curve
from matplotlib import pyplot as plt2
plt2.plot(np.arange(1,6),wcss)
plt2.xlabel('Clusters')
plt2.ylabel('SSE')
plt2.show()

# K = 2 is selected from the elbow function 

#  k-means to fit and predict using the best k value from the elbow method 
km = KMeans(n_clusters=2)
kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(X0,X1)
data["cluster"] = pred_y

from matplotlib import pyplot as plt3
data1 = data["cluster" == 0]
data2 = data["cluster" == 1]

plt3.scatter(data1.X0, data1.X1, color = "blue")
plt3.scatter(data2.X0, data2.X1, color = "Red")

plt3.xlabel("X1")
plt3.ylabel("X2")
plt3.legend
plt3.show()

# Q5 : 	Implement matrix multiplication x*y.
# Program to multiply two matrices using nested loops
import numpy as np

# Matrix 1
X =np.matrix([[1,2,3]])
# matrix 2
Y = np.matrix([[4],[5],[6]])

def multiply_matrix(A,B):
  global C
  if  A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
    for row in range(len(A[0])): 
        for col in range(len(A)):
            for elt in range(len(B)):
              C[row, col] += A[row, elt] * B[elt, col]
    return C
  else:
    return "Sorry, cannot multiply A and B."

print(multiply_matrix(X,Y))

# Q6 : 	Transpose matrix x
import numpy as np
X =np.matrix([[1,2,3],[4,5,6]])
def transpose_matrix(x):
    x_trans = np.empty((len(x[0]),len(x)))
    for i in range(len(x)):
      #Iterate through columns
      for j in range(len(x[0])):
         x_trans[j][i] = x[i][j]
      return x_trans
print(transpose_matrix(X))