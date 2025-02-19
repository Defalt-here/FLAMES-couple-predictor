import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
df = pd.read_csv("speed_data_data.csv")
df.describe()
outcome = df.dec
predictors = df.drop('dec',axis = 1)
xtrain, xtest, ytrain, ytest = train_test_split(predictors,outcome,train_size=0.8,random_state=42)
model = LogisticRegression()
model.fit(xtrain,ytrain)
y_preds = model.predict(xtest)
accuracy = accuracy_score(ytest,y_preds)
print("Accuracy of the model is ",accuracy*100,"%")
array = [1,20,0,6,8,9,9,9,7,7,5,1]
# for i in range(12):
#     s = int(input("Give Input: "))
#     array.append(s)
npArray = np.array(array)
array2D = npArray.reshape(1,12)
answer = model.predict(array2D)
print(answer[0])
filename = "model.sav"
pickle.dump(answer,open(filename,'wb'))