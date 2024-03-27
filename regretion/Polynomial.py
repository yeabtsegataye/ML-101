import matplotlib.pyplot as plt
import pandas as pd
import numpy
from sklearn.metrics import r2_score

data = pd.read_csv('besics/regretion/poly.csv')

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

##########################
#The purpose of setting the degree in polynomial regression is to control the complexity of the fitted polynomial model and to balance between underfitting and overfitting.
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))# 3 is the degree

myline = numpy.linspace(1, 22, 100)# the line start form 1 and end at 22 withe 100 points
##########################
print(r2_score(y, mymodel(x)))# Note: The result 0.94 shows that there is a very good relationship, and we can use polynomial regression in future predictions.
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
# print(int(mymodel(17))) # to predict