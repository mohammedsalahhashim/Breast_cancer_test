# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('E:/work/trained_model.sav', 'rb'))

input_data = (0.08139,0.05667000000000001,0.9429,18.15,0.009282,0.009216,0.020630000000000003,0.008965,0.002146,23.84,78.0,0.129,0.1444,0.24,0.06641)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The tumor is Benign')
else:
  print('The tumor is Malignant')