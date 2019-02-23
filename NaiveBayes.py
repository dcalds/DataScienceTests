import numpy as np
# Samples
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array(([1, 1, 1, 2, 2, 2]))

from sklearn.naive_bayes import GaussianNB
# Classifier
clf = GaussianNB()
# Train
clf.fit(X,Y)
# Prediction from trained model
y_pred = clf.predict([[-0.8,-1],[0.6,-1],[0.9,-0.8],[-1,1.9]])

from sklearn.metrics import accuracy_score
y_true = [1,1,2,2]
# Accuracy
accuracy_score(y_true, y_pred)
# Correct predictions
accuracy_score(y_true, y_pred, normalize=False)
