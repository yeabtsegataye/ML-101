import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# from sklearn import tree
# import matplotlib.pyplot as plt
# import sys

# Read the dataset
df = pd.read_csv("besics/tree/data.csv")

# Convert categorical variables to numerical reference
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

# Separate the dependent and independent variables
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

# Fit the decision tree classifier
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# Print prediction for a sample
print(dtree.predict([[40, 10, 9, 0]]))

# Plot the decision tree
# plt.figure(figsize=(8, 5))
# tree.plot_tree(dtree, feature_names=features)
# plt.savefig(sys.stdout.buffer)
# plt.show()

############## You will see that the Decision Tree gives you different results if you run it enough times, even if you feed it with the same data.
#That is because the Decision Tree does not give us a 100% certain answer. It is based on the probability of an outcome, and the answer will vary.s ########
