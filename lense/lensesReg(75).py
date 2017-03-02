import numpy as np
from numpy import genfromtxt
X = genfromtxt("F:\\6th\\courses\\lenses.data",dtype=float)

x = X[:,:5]
y = X[:,5:]
print x.shape
print y.shape

train = len(X)*.75


xtrain = x[:train]
ytrain = y[:train]

xtest = x[train:]
ytest = y[train:]



from sklearn import linear_model

clf = linear_model.LinearRegression()
clf.fit(xtrain,ytrain)

print clf.predict(xtest[0])
print "\n"
print clf.score(xtest,ytest)*100





