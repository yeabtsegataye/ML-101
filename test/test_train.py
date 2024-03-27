import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)
from sklearn.metrics import r2_score

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

########## check relation ############
r2 = r2_score(train_y, mymodel(train_x))
print(r2) # The result 0.799 shows that there is a OK relationship.

r1 = r2_score(test_y, mymodel(test_x))
print(r1)# The result 0.809 shows that the model fits the testing set as well, and we are confident that we can use the model to predict future values.
########predict ###############
print(mymodel(5))
####################### to see the graph ############

# myline = numpy.linspace(0, 5.5, 100)
# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))
# plt.show()