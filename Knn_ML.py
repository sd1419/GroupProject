from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


path = os.getcwd()
filename = os.path.join(path,'Subject_1.xlsx')

# reading in the excel file and editting the time column
df = pd.read_excel(filename)
df['Elapsed time'] = df['Elapsed time'].str.replace("'", "")
df['Elapsed time'] = pd.to_datetime(df['Elapsed time'], format='%M:%S.%f')
df['Elapsed time'] = (df['Elapsed time']-pd.Timestamp('1970-01-01'))//pd.Timedelta('1s')
print(df['Elapsed time'])

# Split dataframe to create the features and target values
X = df[['Elapsed time','SpO2','hr']].values
y = df['label'].values

# Build a pipeline and use cross validation as well as scaling to see if the accuracy increases
steps = [('scaler',StandardScaler()),('knn',KNeighborsClassifier(n_neighbors = 42))]
pipeline = Pipeline(steps)
parameters = {"knn__n_neighbors": np.arange(1,50)}
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3, random_state= 21)

cv = GridSearchCV(pipeline,param_grid=parameters)
cv.fit(X_train,y_train)
knn_scaled = pipeline.fit(X_train,y_train)

#Make predictions using scaled model and scaled and cv model
# in order to compare accuracies
pred_cv = cv.predict(X_test)
pred = knn_scaled.predict(X_test)
print('The score using scaled, cv model is' , cv.best_score_)
print(cv.best_params_)
print('The score using scaled model is' , knn_scaled.score(X_test,y_test))

# Load new data and make predictions
new_data = np.array([[80, 95,2208986506], [90, 92,2208986556], [85, 90,2208988900],[95,82,2208987865]])
predictions = cv.predict(new_data)
print(predictions)

"""
without scaling the data
#Accuracy - number of correct observation to total numb of obs
#To choose neighbors we need to balance between overfitting and underfitting
# low k is more suceptive to noise and high k is less accurate, a simpler model
# Plot the accuracies to choose k
# If the training accuracy is much greater than the testing - overfitting
# Best k is where testing is highest and there is smalles gap between the 2 """
train_accuracies = {}
test_accuracies = {}
neighbors = np.arange(1,26)

for neighbor in neighbors:
    knn = KNeighborsClassifier(n_neighbors = neighbor)
    knn.fit(X_train,y_train)
    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)


plt.plot(neighbors, train_accuracies.values(), label = 'Training Accuracy')
plt.plot(neighbors, test_accuracies.values(), label = 'Testing Accuracy')
plt.legend()
plt.xlabel('Number of neighbors')
plt.ylabel('Accuracy')
plt.title('Accuracy of training and testing data with number of neighbours')
plt.show()

