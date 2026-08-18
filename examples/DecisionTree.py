# ---------------------------------------- #
## Notebooks can be used to run sections of script
## and keep the results in memory

## Scripts, on the other hand, run once and forget everything
# ---------------------------------------- #

# ---------------------------------------- #
# Basic imports
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import pandas as pd
# ---------------------------------------- #

# ---------------------------------------- #
# Data shared among models #
# Data loading
data = sklearn.datasets.load_breast_cancer(as_frame=True)
data_as_DataFrame = data.frame
# Alias to something easier to work with
df = data_as_DataFrame
# ---------------------------------------- #

# ---------------------------------------- #
# Local requirements
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# ---------------------------------------- #

# ---------------------------------------- #
# Re-sample the original data and perform a train(ing)/80%, test(ing)/20% data split
x = data.data
y = data.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# ---------------------------------------- #

# ---------------------------------------- #
# Initialize the classifier
tree_classifier = DecisionTreeClassifier(max_depth=5, random_state=42)
# Fit data within the classifier
tree_classifier.fit(x_train, y_train)
# Obtain predictions from the classifier
label_prediction = tree_classifier.predict(x_test)
# Chack for overall accuracy with sklearn's built-in tool
accuracy = accuracy_score(y_test, label_prediction)
# Print out the result
# Note the ":.2f" - this tells python to round (the floating-point) 
# to 2 decimal places
print(f"Tree accuracy: {accuracy * 100:.2f}%")
# ---------------------------------------- #

# ---------------------------------------- #
# Plot what form the tree takes
fig = plot_tree(tree_classifier)
# The command line isn't able to view images at the terminal
plt.savefig("decision_tree.png")
# ---------------------------------------- #
