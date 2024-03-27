#Multiple regression is like linear regression, but with more than one independent value, meaning that we try to predict a value based on two or more variables.
import pandas as ps
from sklearn import linear_model



data = ps.read_csv('besics/regretion/data.CSV')

X = data[['Weight', 'Volume']] # independent variable 
y = data['CO2'] # dependent variable on the weight and volume of the car

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[2300, 1300]]) # prediction by inputting weight and volume

print(predictedCO2)