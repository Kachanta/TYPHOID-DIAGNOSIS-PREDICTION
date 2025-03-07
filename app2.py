# Importing Necessary libraries
import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Load the model
with open('typhoid_model2.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("Typhoid Diagnosis Prediction App")
st.write("**Typhoid fever remains a significant public health challenge in many parts of the world, particularly in developing countries where access to clean water and sanitation is limited. With the rise of antibiotic-resistant strains of Salmonella typhi, the bacterium responsible for typhoid fever, there's a need for innovative approaches to diagnose, treat, and manage this disease effectively.**")
st.write("This app classifies the outcome of treatments based on a combination of patient symptoms, laboratory test results, and prescribed medications. By leveraging machine learning algorithms trained on historical patient diagnostic data, the model can predict whether a treatment is likely to be successful, or not.\n\nPlease input the following parameters:")

# Creating the form to collect user inputs
with st.form(key='typhoid_form'):
    age = st.number_input('Age', min_value=0, max_value=100, value=30)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    symptoms_severity = st.selectbox('Symptoms Severity',[ 'Low', 'Moderate', 'High'])
    hemoglobin = st.number_input('Hemoglobin (g/dL)', min_value=10., max_value=25.0, value=15.0)
    platelet_count = st.number_input('Platelet Count', min_value=150000, max_value=450000, value=250000)
    blood_culture_bacteria = st.selectbox('Blood Culture Bacteria', ['Staphylococcus', 'Escherichia coli', 'Salmonella typhi', 'Others',])

    # Urine Culture Bacteria (Binary input or categorical)
    urine_culture_bacteria = st.selectbox('Urine Culture Bacteria', ['Escherichia coli', 'Klebsiella pneumoniae','Others'])

    # Calcium (mg/dL)
    calcium = st.number_input('Calcium (mg/dL)', min_value=0.0, max_value=15.0, value=9.5)

    # Potassium (mmol/L)
    potassium = st.number_input('Potassium (mmol/L)', min_value=0.0, max_value=10.0, value=4.0)

    # Current Medication
    current_medication = st.selectbox('Current Medication', ['Amoxicillin','Azithromycin','Ceftriaxone'])

    # Treatment Duration (in days)
    treatment_duration = st.number_input('Treatment Duration (days)', min_value=0, max_value=15, value=7)

    # Treatment Outcome (Assumed binary: Success or Failure)
    #treatment_outcome = st.selectbox('Treatment Outcome', ['Success', 'Failure'])

    # Submit button
    submit_button = st.form_submit_button(label='Predict')

# Handling the prediction
if submit_button:
    # Preprocessing the inputs into the correct format for the model
    inputs = {
        'Age': age,
        'Gender': 1 if gender == 'Male' else 0,
        'Symptoms Severity': 0 if symptoms_severity== 'Low' else 1 if symptoms_severity == 'Moderate' else 2,
        'Hemoglobin (g/dL)': hemoglobin,
        'Platelet Count': platelet_count,
        'Blood Culture Bacteria': 1 if blood_culture_bacteria == 'Staphylococcus' else 2 if blood_culture_bacteria == 'Escherichia coli' else 3 if blood_culture_bacteria == 'Salmonella typhi' else 4,
        'Urine Culture Bacteria': 1 if urine_culture_bacteria == 'Escherichia coli' else 2 if urine_culture_bacteria == 'Klebsiella pneumoniae' else 3,
        'Calcium (mg/dL)': calcium,
        'Potassium (mmol/L)': potassium,
        'Current Medication': 1 if current_medication== 'Amoxicillin' else 2 if current_medication == 'Azithromycin' else 3,
        'Treatment Duration': treatment_duration,
        #'Treatment Outcome': 1 if treatment_outcome == 'Success' else 0
    }


    # Creating a dataframe from inputs for the model prediction
    input_df = pd.DataFrame([inputs])

    # Model Prediction
    prediction = model.predict(input_df)

    # Display the result
    if prediction == 1:
        st.write("**Prediction: The patient RECOVERED.**")
    else:
        st.write("**Prediction: The patient DID NOT RECOVER.**")

    # Optionally, you can display additional information or visualization here based on model output

