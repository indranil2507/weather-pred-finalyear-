

# import the libraries
from operator import index
from turtle import clear
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# read the cleaned data
data = pd.read_csv("dataset_ml.csv")

#separate the dependant and independant values in the cleaned data(here total precipitation in a day is dependant;
# whereas the rest are dependant)

X = data.drop(['date','tot'], axis=1)

Y = data['tot']


#divide the data into train and test in 80-20 ratio

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

#train the model
clf = LinearRegression()
clf.fit(X_train, Y_train)

#predict the values for test variables and compare with actual actual outputs of test in a df , plot a graph;
#display training and testing scores to check accuracy of model

Yp=clf.predict(X_test)


y_test_predict=pd.DataFrame({"Y_actual":Y_test,"Y_predict":Yp})
y_test_predict['index-a'] = range(1,len(y_test_predict)+1)


print(y_test_predict)

print('Train Score:',clf.score(X_train,Y_train))
print('Test Score:',clf.score(X_test,Y_test))

y_test_predict.plot(x='index-a',y=["Y_actual","Y_predict"])
plt.show()

# predict output of real time data.

inp = np.array([[35],[28],[61],[1003],[0.6]])

inp = inp.reshape(1, -1)

# Print output
print('The precipitation in mm for the input is:', clf.predict(inp))






