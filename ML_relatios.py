import matplotlib.pyplot as plt
from scipy import stats
# import numpy
x = [18,19,20,21,22,23,24]
y = [3,4,4,8,9,15,24]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

# mymodel = list(map(myfunc, x))

test = myfunc(38)
print(test)