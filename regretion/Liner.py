import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
data = pd.read_csv('besics/regretion/liner.csv')


x = data['Study_Time']
y = data['Score'] # our dependent variable

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))
############ this is for pridicting 6hr study_time ###############

# score = myfunc(8)
# print(int(score))
################################################
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()