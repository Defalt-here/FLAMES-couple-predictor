import numpy as np
import pickle
loaded_model = pickle.load(open("model.sav","rb"))
array = [1,20,0,6,8,9,9,9,7,7,5,1]
npArray = np.array(array)
array2D = npArray.reshape(1,12)
print(loaded_model[0])