#Created By Matthew Li
#06/13/18

#Gender Classifier Based on Measurements

from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree

#height, weight, shoe size
X = [[181, 80, 44],[177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,47], [175,64,39], [177,70,40],[159,55,37], [171,75,42], [181,85,43]]
#gender
Y = ["male", "female", "female", "female", "male", "male", "male", "female", "male", "female", "male"]

#Decision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

prediction = clf.predict([[190,70,43]]) #male
print prediction

#KNearestNeighbor
import numpy as np
clf2 = KNeighborsClassifier(n_neighbors=3)
clf2 = clf2.fit(X,Y)

prediction2 = clf2.predict([[190,70,43]]) #male
print prediction2

#SVM
from sklearn import svm
clf3 = svm.SVC()
clf3.fit(X,Y)

prediction3 = clf3.predict([[190,70,43]]) #male
print prediction3