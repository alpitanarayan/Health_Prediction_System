import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Set page configuration
st.set_page_config(page_title = "Health Guard",layout = "wide")

# Setting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/heart_disease_model.sav','rb'))

parkinsons_disease_model = pickle.load(open(f'{working_dir}/parkinsons_disease_model.sav','rb'))

# Sidebar for navigation

with st.sidebar:
	selected = option_menu("Multiple Disease Prediction System",['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Disease Prediction'],menu_icon = 'hospital-fill', icons = ['activity','heart','person'],default_index = 0)


# Diabetes Prediction page

if selected == 'Diabetes Prediction':
	
	# Title of the page
	st.title('Diabetes Prediction Using ML')
	
	# setting up of the number of the columns with the name 
	col1, col2, col3 = st.columns(3)
	
	with col1:
		pregnancies = st.text_input("Number of Pregnancies")
		
	with col2:
		glucose = st.text_input("Glucose Level")
	
	with col3:
		bloodpressure = st.text_input("Blood Pressure Value")
	
	with col1:
		skinthickness = st.text_input("Skin Thickness Value")
	
	with col2:
		insulin = st.text_input("Insulin Level")

	with col3:
		bmi = st.text_input("BMI Value")
	
	with col1:
		diabetespedigreefunction = st.text_input("Diabetes Pedigree Function Value")
	
	with col2:
		Age = st.text_input("Age of the Person")
	
	# Code for Prediction 
	diab_diagnosis = ''
	
	# Creation of the button
	
	if st.button('Diabetes Test Result'):
		user_input = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, Age]
		
		user_input = [float(x) for x in user_input]
			
		diab_prediction = diabetes_model.predict([user_input])        # again we put the user_input list so that it can convert it into 2-D array
		
		if diab_prediction[0] == 1:
			diab_diagnosis = "The Person is Diabetic!!"
		else:
			diab_diagnosis = 'The Person is not Diabetic!!'
		
	st.success(diab_diagnosis)


# Diabetes Prediction page


if selected == 'Heart Disease Prediction':

	# Title of the page

	st.title('Heart Disease Prediction using ML')
	coll1, coll2, coll3 = st.columns(3)

	with coll1:
		Age = st.text_input("Age of the Person")
	with coll2:
		Sex = st.text_input("Gender")
	with coll3:
		cd = st.text_input("Constrictive pericarditis")

	with coll1:
		bp = st.text_input("Resting Blood Pressure")
	
	with coll2:
		serum = st.text_input("Serum Cholestoral in mg/dl")
	with coll3:
		fasting_blood_sugar = st.text_input("Fasting Blood Sugar > 120 mg/dl")
	
	with coll1:
		electrocardiographic = st.text_input("Resting Electrocardiographic result")
	with coll2:
		heart_rate = st.text_input("Maximum Heart Rate achieved")
	with coll3:
		exercise = st.text_input("Exercise Induced Angina")

	with coll1:
		st_depression = st.text_input("ST depression induced by exercise")
	with coll2:
		slope_of_peak_exercise = st.text_input("Slope of the peak exercise ST segment")
	with coll3:
		vessel_color = st.text_input("Major vessel colored by flourosopy")

	with coll1:
		some_essentials = st.text_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect ")		

#code for prediction
	heart_diagnosis = ''

	if st.button("Heart Disease Test Result"):
		user_input2 = [Age, Sex, cd, bp, serum, fasting_blood_sugar, electrocardiographic, heart_rate, exercise, st_depression, slope_of_peak_exercise, vessel_color, some_essentials]

		user_input2 = [float(x) for x in user_input2]
		
		heart_prediction = heart_disease_model.predict([user_input2])

		if heart_prediction[0] == 1:
			heart_diagnosis = "The Person have chance of heart attack!!"

		else:
			heart_diagnosis = "The Person have no chance of heart attack!!"
	


	st.success(heart_diagnosis)




# Parkinsons disease Prediction page 
# ==================================

if selected == "Parkinsons Disease Prediction":

    #Title of the page
    st.title('Parkison Disease Prediction using ML')
    cul1, cul2, cul3, cul4, cul5 = st.columns(5)

    with cul1:
        mdvp_fo = st.text_input("MDVP:Fo(Hz)")
    with cul2:
        mdvp_fhi = st.text_input("MDVP:Fhi(Hz)")
    with cul3:
        mdvp_flo = st.text_input("MDVP:Flo(Hz)")
    with cul4:
        mdvp_jitter_per = st.text_input("MDVP:Jitter(%)")
    with cul5:
        mdvp_jiiter_abs = st.text_input("MDVP:Jitter()Abs")

    
    with cul1:
        mdvp_rap = st.text_input("MDVP:RAP")
    with cul2:
        mdvp_ppq = st.text_input("MDVP:PPQ")
    with cul3:
        jitter_ddp = st.text_input("Jitter:DDP")
    with cul4:
        mdvp_shimmer = st.text_input("MDVP:Shimmer")
    with cul5:
        mdvp_shimmer_db = st.text_input("MDVP:Shimmer(dB)")

    
    with cul1:
        shimmer_apq3 = st.text_input("Shimmer:APQ3")
    with cul2:
        shimmer_apq5 = st.text_input("Shimmer:APQ5")
    with cul3:
        mdvp_apq = st.text_input("MDVP:APQ")
    with cul4:
        shimmer_dda = st.text_input("Shimmer:DDA")
    with cul5:
        nhr = st.text_input("NHR")
        

    with cul1:
        hnr = st.text_input("HNR")
    with cul2:
        rpde = st.text_input("RPDE")
    with cul3:
        dfa = st.text_input("DFA")
    with cul4:
        spread1 = st.text_input("shread1")
    with cul5:
        spread2 = st.text_input("shread2")

    with cul1:
        d2 = st.text_input("D2")
    with cul2:
        ppe = st.text_input("PPE")

    # Code for Prediction

    parkinsons_diagnosis = ''

    if st.button("Parkinson Test Result"):
        user_input3 = [mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitter_per, mdvp_jiiter_abs, mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]

        user_input3 = [float(x) for x in user_input3]

        parkinsons_pred = parkinsons_disease_model.predict([user_input3])

        if parkinsons_pred[0] == 1:
            parkinsons_diagnosis = "Person have chances of Parkinsons"
        else:
            parkinsons_diagnosis = "Person have no chances of Parkinsons "

    st.success(parkinsons_diagnosis)




















