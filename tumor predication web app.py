# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 01:35:37 2022

@author: MOHAMMED
"""
import numpy as np
import pickle
import streamlit as st

#
# loading the saved model
loaded_model = pickle.load(open('E:/work/trained_model.sav', 'rb'))

def tumor_prediction(input_data):
    
    
        # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The tumor is Benign'
    else:
      return 'The tumor is Malignant'
  

    
     
def main():
    
    
    # giving a title
    st.title(' Web App of Prediction The Breast Cancer Tumor Type  ')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        smoothness_mean = st.text_input('smoothness_mean')
        
    with col2:
        fractal_dimension_mean = st.text_input('fractal_dimension_mean')
    
    with col3:
        texture_se = st.text_input('texture_se')
    
    with col1:
        area_se = st.text_input('area_se')
    
    with col2:
        smoothness_se = st.text_input('smoothness_se')
        
    with col3:
        compactness_se = st.text_input('compactness_se')
         
    with col1:
        concavity_se = st.text_input('concavity_se')
     
    with col2:
        concavepoints_se = st.text_input('concave points_se')
     
    with col3:
        fractal_dimension_se = st.text_input('fractal_dimension_se')
     
    with col1:
        texture_worst = st.text_input('texture_worst')
    
    with col2:
        perimeter_worst = st.text_input('perimeter_worst')
         
    with col3:
        smoothness_worst = st.text_input('smoothness_worst')
     
    with col1:
        concavity_worst = st.text_input('concavity_worst')
     
    with col2:
        symmetry_worst = st.text_input('symmetry_worst')
     
    with col3:
        fractal_dimension_worst = st.text_input('fractal_dimension_worst') 
    
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Cancer Test Result'):
        diagnosis = tumor_prediction([float(smoothness_mean), float(fractal_dimension_mean), float(texture_se), float(area_se), float(smoothness_se), float(compactness_se), float(concavity_se), float(concavepoints_se),float(fractal_dimension_se),float(texture_worst),float(perimeter_worst),float(smoothness_worst),float(concavity_worst),float(symmetry_worst),float(fractal_dimension_worst)])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
  