import numpy as np
import pickle
loaded_model = pickle.load(open("newModel.sav","rb"))
array = [1,20,10,10,10,10,10,10,10,10,1] #0,21,3,8,9,6,10,7,8,6,1
npArray = np.array(array)
array2D = npArray.reshape(1,11)
prediction = loaded_model.predict(array2D)
print(prediction)