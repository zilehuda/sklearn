import numpy as np
from numpy import genfromtxt
X = genfromtxt("F:\\6th\\courses\\ballon.data" , delimiter=',', dtype=str)



x = X[:,:4]
y = X[:,4]

hold1=x[:,0]
hold2=x[:,1]
hold3=x[:,2]
hold4=x[:,3]


array1=[0 for a in range(0,len(hold1))]
array2=[0 for b in range(0,len(hold2))]
array3=[0 for c in range(0,len(hold3))]
array4=[0 for c in range(0,len(hold4))]
array5=[0 for d in range(0,len(y))]

dic1={}
dic2={}
dic3={}
dic4={}
dic5={}

val1=0
for i in range(0, len(hold1)):
    if hold1[i] not in dic1:
        dic1[hold1[i]]=val1
        val1=val1+1
    array1[i]=dic1[hold1[i]]

val2=0
for i in range(0, len(hold2)):
    if hold2[i] not in dic2:
        dic2[hold2[i]]=val2
        val2=val2+1
    array2[i]=dic2[hold2[i]]

val3=0
for i in range(0, len(hold3)):
    if hold3[i] not in dic3:
        dic3[hold3[i]]=val3
        val3=val3+1
    array3[i]=dic3[hold3[i]]


val4=0
for i in range(0, len(hold4)):
    if hold4[i] not in dic4:
        dic4[hold4[i]]=val4
        val4=val4+1
    array4[i]=dic4[hold4[i]]

val5=0
for i in range(0, len(y)):
    if y[i] not in dic5:
        dic5[y[i]]=val5
        val5=val5+1
    array5[i]=dic5[y[i]]


hold1=np.array(array1)
hold2=np.array(array2)
hold3=np.array(array3)
hold4=np.array(array4)

for i in range(0,len(x)):
	x[i,0]=hold1[i]
for i in range(0,len(x)):
	x[i,1]=hold2[i]
for i in range(0,len(x)):
	x[i,2]=hold3[i]
for i in range(0,len(x)):
	x[i,3]=hold4[i]


y=np.array(array5)
x=x.astype(int)

train = len(x)*.75

xtrain = x[:train]
ytrain = y[:train]
xtest = x[train:]
ytest = y[train:]

from sklearn import linear_model

clf = linear_model.LinearRegression()


clf.fit(xtrain,ytrain)


print clf.score(xtest,ytest)
