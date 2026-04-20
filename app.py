import streamlit as st
import pandas as pd
import joblib

# Load the trained model
# Make sure 'random_forest_model.pkl' is in the same directory as this app.py file
model = joblib.load('random_forest_model.pkl')

st.title('Salary Prediction App')
st.write('Enter the details below to predict the salary.')

# Input features
education_options = {0: 'High School', 1: 'Bachelor\'s', 2: 'Master\'s', 3: 'PhD'}
education = st.selectbox('Education Level', options=list(education_options.keys()), format_func=lambda x: education_options[x])

experience = st.slider('Years of Experience', 0, 30, 5)

location_options = {0: 'Rural', 1: 'Urban', 2: 'Suburban'}
location = st.selectbox('Location', options=list(location_options.keys()), format_func=lambda x: location_options[x])

job_title_options = {0: 'Junior Developer', 1: 'Senior Developer', 2: 'Manager', 3: 'Analyst'}
job_title = st.selectbox('Job Title', options=list(job_title_options.keys()), format_func=lambda x: job_title_options[x])

age = st.slider('Age', 18, 70, 30)

gender_options = {0: 'Female', 1: 'Male'}
gender = st.selectbox('Gender', options=list(gender_options.keys()), format_func=lambda x: gender_options[x])


if st.button('Predict Salary'):
    # Create a DataFrame from user input
    input_data = pd.DataFrame([[education, experience, location, job_title, age, gender]],
                              columns=['Education', 'Experience', 'Location', 'Job_Title', 'Age', 'Gender'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.success(f'The predicted salary is: ${prediction:,.2f}')
