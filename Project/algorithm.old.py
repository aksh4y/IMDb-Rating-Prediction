#Import Library
import warnings
import numpy as np
import datetime
from extract_data import *
from word_encoder import *
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

# send the extracted data availble from extract_data to the encode function
# this function vectorizes the text based data into ASCII format for use by
# the algorithms
encoded_data = encode(data)

scores = []

# convert the float scores to int. Multiplying by 10 helps us keep the decimal
# level precision which would otherwise be lost in typecasting
i = 0
while i < len(label):
    scores.append(int (float(label[i]) * 10))
    i += 1;

# ignore depricated warning
def warn(*args, **kwargs):
    pass
warnings.warn = warn

# SVM classifier
svm_clf = svm.SVC(kernel = 'linear')
#svm_clf.fit(encoded_data, scores)

# Gaussian Naive Bayes
gnb_clf = GaussianNB()
gnb_clf.fit(encoded_data, scores)

# Random Forest
rf_clf = RandomForestClassifier(n_estimators=10)
rf_clf.fit(encoded_data, scores)

# Decision Tree
dt_clf = tree.DecisionTreeClassifier()
dt_clf.fit(encoded_data, scores)


#print("SVM:")

#print(svm_clf.predict ([1403, 2752, 3263, 4200, 4309, 4417, 4518, 4675, 5909, 6102, 6500, 8459, 8672, 8882, 9712, 9810, 10524, 10757, 11096, 11299, 11461, 11617, 11775]))

print("Gaussian Naive Bayes:")

print(gnb_clf.predict ([1403, 2752, 3263, 4200, 4309, 4417, 4518, 4675, 5909, 6102, 6500, 8459, 8672, 8882, 9712, 9810, 10524, 10757, 11096, 11299, 11461, 11617, 11775]))

print("Random Forest:")

print(rf_clf.predict ([1403, 2752, 3263, 4200, 4309, 4417, 4518, 4675, 5909, 6102, 6500, 8459, 8672, 8882, 9712, 9810, 10524, 10757, 11096, 11299, 11461, 11617, 11775]))

print("Decision Tree:")

print(dt_clf.predict ([1403, 2752, 3263, 4200, 4309, 4417, 4518, 4675, 5909, 6102, 6500, 8459, 8672, 8882, 9712, 9810, 10524, 10757, 11096, 11299, 11461, 11617, 11775]))

print("End time: " + str(datetime.datetime.now()).split('.')[0])
