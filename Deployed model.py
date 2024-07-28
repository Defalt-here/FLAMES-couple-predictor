import numpy as np
import pickle
loaded_model = pickle.load(open("newModel.sav","rb"))
array = [1,20,6,9,8,5,10,5,7,6,1]
npArray = np.array(array)
array2D = npArray.reshape(1,11)
print(loaded_model)