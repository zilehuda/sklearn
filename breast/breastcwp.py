import numpy as np
from numpy import genfromtxt


X = genfromtxt("F:\\6th\\courses\\breast-cancer-wisconsin.data",delimiter=",",dtype=int)

x = X[:,:10]
y = X[:,10:]

train = len(X)*.75

xtrain = x[:train]
ytrain = y[:train]

xtest = x[train:]
ytest = y[train:]

print ytest.shape

from sklearn import linear_model

clf = linear_model.LinearRegression()

clf.fit(xtrain,ytrain)

print clf.score(xtest,ytest)*100








