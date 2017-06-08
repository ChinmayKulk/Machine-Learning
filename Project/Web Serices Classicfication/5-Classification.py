__author__ = 'chinmay'


import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

#path to the final matrix obtained by multiplying semantic similarity matrix and TF-IDF matrix
input_file = "C:/Users/chinmay/Desktop/ws/FinalMultipliedData.csv"


#reading the file as pandas frame
df = pd.read_csv(input_file)


#feature sets of the data
features=list(df.columns[:-1])

#SPliting the data between for training and testing
df_train=df.sample(frac=0.8,random_state=200)
df_test=df.drop(df_train.index)




#creating training set
x_train = df_train[features]
y_train=df_train.Category.replace({'communication':0,'food':1,'weapon':2,'geography':3,'education':4,'medical':5,'simulation':6,'travel':7,'economy':8})

#creating Testing set
x_test = df_test[features]
y_test=df_test.Category.replace({'communication':0,'food':1,'weapon':2,'geography':3,'education':4,'medical':5,'simulation':6,'travel':7,'economy':8})


#Decision tree classifier results
print("Decision Tree:")
dtree=DecisionTreeClassifier(random_state=0,max_depth=20)
dtree.fit(x_train,y_train)
print("The accuracy for Decision tree Classifier is: "+str((metrics.accuracy_score(y_test,dtree.predict(x_test)))*100)+"%")
print("-------------------------------------------------------------------------------------------------------------------")
print()

#Naive Bayes classifier results
print("Naive Bayes:")
Nb=MultinomialNB()
Nb.fit(x_train,y_train)
print("The accuracy for Naive Bayes Classifier is: "+str((metrics.accuracy_score(y_test,Nb.predict(x_test)))*100)+"%")
print("-------------------------------------------------------------------------------------------------------------------")
print()

#Random Forest classifier results
print("Random Forest:")
Rf=RandomForestClassifier(n_estimators=500,max_depth=20)
Rf.fit(x_train,y_train)
print("The accuracy for Random Forest Classifier is: "+str((metrics.accuracy_score(y_test,Rf.predict(x_test)))*100)+"%")
print("-------------------------------------------------------------------------------------------------------------------")
print()


#MultiLayer Perceptron Classification Results
print("Multilayer Perceptron:")
ANN=MLPClassifier()
ANN.fit(x_train,y_train)
print("The accuracy for MLP Classifier is: "+str((metrics.accuracy_score(y_test,ANN.predict(x_test)))*100)+"%")
print("-------------------------------------------------------------------------------------------------------------------")
print()

#K nearest neighbor CLassifier results
print("K nearest neighbor:")
KNN=KNeighborsClassifier(n_neighbors=6,algorithm='auto')
KNN.fit(x_train,y_train)
print("The accuracy for KNN Classifier is: "+str((metrics.accuracy_score(y_test,KNN.predict(x_test)))*100)+"%")
print("-------------------------------------------------------------------------------------------------------------------")
print()


























































