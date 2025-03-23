from sklearn import tree
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier 

clf = tree.DecisionTreeClassifier()
clf2 = svm.SVC()
knnclf = KNeighborsClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42],
     [181, 85, 43], [168, 72, 41], [182, 88, 45], [158, 50, 35], [176, 74, 42],
     [185, 92, 46], [163, 58, 37], [169, 63, 39], [178, 76, 42], [186, 95, 47],
     [157, 52, 36], [174, 67, 40], [180, 83, 44], [155, 49, 34], [172, 78, 41],
     [161, 59, 38], [184, 90, 46], [167, 66, 39], [170, 71, 40], [188, 94, 48]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male', 'female', 'male', 'female', 'male', 'male',
     'female', 'female', 'male', 'male', 'female', 'male', 'male', 'female',
     'female', 'male', 'male', 'female', 'male', 'male']


# CHALLENGE - ...and train them on our data

clf = clf.fit(X, Y)
clf2 = clf2.fit(X, Y)
knnclf = knnclf.fit(X,Y)
prediction_svm = clf2.predict([[190, 90, 46]])

prediction_tree = clf.predict([[160, 30, 36]])

prediction_knn = knnclf.predict([[160, 30, 36]])


##print result
print("decision tree:" + prediction_tree)
print("SVM:" +prediction_svm)
print("KNN:" +prediction_knn)