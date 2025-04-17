# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 18:00:55 2025

@author: OLADOYINBO BABATUNDE
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/OLADOYINBO BABATUNDE/trained_model.sav', 'rb'))

#Creating a function 
def hyper_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
        return 'The person is not Hypertensive'
    else:
        return 'The person has possibility of Hypertension'
    
    

def main():
    
    
    st.title('Hypertension Status Prediction')
    
    BMI = st.number_input("Please Enter yuor BMI value: ")
    PhysicalHealth = st.number_input("In 30 days of the month, on the average, how many days are you Physically active? ")
    MentalHealth = st.number_input("In 30 days of the month, on the average, how many days are you Mentally active? ")
    SleepTime = st.number_input("How many hours do you averagelly sleep in a day? ")
    
    Is_Smoking = st.radio("Do you smoke? ", ['Yes', 'No'])
    if Is_Smoking.lower() == 'yes':
        Smoking_Yes = 1
    else:
        Smoking_Yes = 0
        
    Is_Alcohol = st.radio("Do you drink alcohol? ", ['Yes', 'No'])
    if Is_Alcohol.lower() == 'yes':
        AlcoholDrinking_Yes = 1
    else:
        AlcoholDrinking_Yes = 0
        
    Is_Stroke = st.radio("Do you suffer from stroke? ", ['Yes', 'No'])
    if Is_Stroke.lower() == 'yes':
        Stroke_Yes = 1
    else:
        Stroke_Yes = 0   

    Is_Diff_Walking = st.radio("Do you have difficulty walking? ", ['Yes', 'No'])
    if Is_Diff_Walking.lower() == 'yes':
        DiffWalking_Yes = 1
    else:
        DiffWalking_Yes = 0    

    Is_Sex = st.radio("Sex? ", ['Male', 'Female'])
    if Is_Sex.lower() == 'male':
        Sex_Male = 1
    else:
        Sex_Male = 0

    what_age = st.number_input("Please Enter your age: ")
    if (what_age >= 25) & (what_age <= 29):
        AgeCategory_25_29 = 1; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 30) & (what_age <= 34):
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 1; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 35) & (what_age <= 39):
       AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 1; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
       AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 40) & (what_age <= 44):
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 1; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 45) & (what_age <= 49):
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 1; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 50) & (what_age <= 54):
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 1; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 55) & (what_age <= 59):
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 1; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 60) & (what_age <= 64):
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 1; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 65) & (what_age <= 69):
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 1; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 70) & (what_age <= 74):
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 1; AgeCategory_75_79 = 0; AgeCategory_80_or_older =0
    elif (what_age >= 75) & (what_age <= 79):
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 1; AgeCategory_80_or_older =0
    elif what_age >= 80:
        AgeCategory_25_29 = 0; AgeCategory_30_34 = 0; AgeCategory_35_39 = 0; AgeCategory_40_44 = 0; AgeCategory_45_49 = 0; AgeCategory_50_54 = 0; 
        AgeCategory_55_59 = 0; AgeCategory_60_64 = 0; AgeCategory_65_69 = 0; AgeCategory_70_74 = 0; AgeCategory_75_79 = 0; AgeCategory_80_or_older =1

    Is_Diabetic = st.radio("Diabetic Status ", ['No','No, borderline diabetes', 'Yes', 'Yes (during pregnancy)'])
    if Is_Diabetic.lower() == 'no, borderline diabetes':
        Diabetic_No_borderline_diabetes = 1; Diabetic_Yes = 0; Diabetic_Yes_during_pregnancy = 0
    elif Is_Diabetic.lower() == 'yes':
        Diabetic_No_borderline_diabetes = 0; Diabetic_Yes = 1; Diabetic_Yes_during_pregnancy = 0
    elif Is_Diabetic.lower() == 'yes (during pregnancy)':
        Diabetic_No_borderline_diabetes = 0; Diabetic_Yes = 0; Diabetic_Yes_during_pregnancy = 1
    elif Is_Diabetic.lower() == 'no':
        Diabetic_No_borderline_diabetes = 0; Diabetic_Yes = 0; Diabetic_Yes_during_pregnancy = 0

    Is_Physical_Activities = st.radio("Do you engage in Physical Activities? ", ['Yes', 'No'])
    if Is_Physical_Activities.lower() == 'yes':
        PhysicalActivity_Yes = 1
    else:
        PhysicalActivity_Yes = 0
        
    Is_GenHealth = st.radio("How do you rate you general health? ", ['Fair', 'Good', 'Poor', 'Very good', 'Excellent'])
    if Is_GenHealth.lower() == 'fair':
        GenHealth_Fair = 1; GenHealth_Good = 0; GenHealth_Poor = 0; GenHealth_Very_good = 0
    elif Is_GenHealth.lower() == 'good':
        GenHealth_Fair = 0; GenHealth_Good = 1; GenHealth_Poor = 0; GenHealth_Very_good = 0
    elif Is_GenHealth.lower() == 'poor':
        GenHealth_Fair = 0; GenHealth_Good = 0; GenHealth_Poor = 1; GenHealth_Very_good = 0
    elif Is_GenHealth.lower() == 'very good':
        GenHealth_Fair = 0; GenHealth_Good = 0; GenHealth_Poor = 0; GenHealth_Very_good = 1
    elif Is_GenHealth.lower() == 'excellent':
        GenHealth_Fair = 0; GenHealth_Good = 0; GenHealth_Poor = 0; GenHealth_Very_good = 0
        
    Is_Asthma = st.radio("Do you have Asthma? ", ['Yes', 'No'])
    if Is_Asthma.lower() == 'yes':
        Asthma_Yes = 1
    else:
        Asthma_Yes = 0
        
    Is_KidneyDisease = st.radio("Do you have Kidney Disease? ", ['Yes', 'No'])
    if Is_KidneyDisease.lower() == 'yes':
        KidneyDisease_Yes = 1
    else:
        KidneyDisease_Yes = 0
        
    Is_SkinCancer = st.radio("Do you have Skin Cancer? ", ['Yes', 'No'])
    if Is_SkinCancer.lower() == 'yes':
        SkinCancer_Yes = 1
    else:
        SkinCancer_Yes = 0
        
    Is_Tribe = st.radio("Tribe ", ['Ibibio', 'Igbo', 'Other', 'Tiv', 'Yoruba'])
    if Is_Tribe.lower() == 'ibibio':
        Tribe_Ibibio = 1; Tribe_Igbo = 0; Tribe_Other = 0; Tribe_Tiv = 0; Tribe_Yoruba = 0
    elif Is_Tribe.lower() == 'igbo':
        Tribe_Ibibio = 0; Tribe_Igbo = 1; Tribe_Other = 0; Tribe_Tiv = 0; Tribe_Yoruba = 0
    elif Is_Tribe.lower() == 'other':
        Tribe_Ibibio = 0; Tribe_Igbo = 0; Tribe_Other = 1; Tribe_Tiv = 0; Tribe_Yoruba = 0
    elif Is_Tribe.lower() == 'tiv':
        Tribe_Ibibio = 0; Tribe_Igbo = 0; Tribe_Other = 0; Tribe_Tiv = 1; Tribe_Yoruba = 0
    elif Is_Tribe.lower() == 'yoruba':
        Tribe_Ibibio = 0; Tribe_Igbo = 0; Tribe_Other = 0; Tribe_Tiv = 0; Tribe_Yoruba = 1
        
    if round(BMI,1) < 18.5:
        BMI_Status_High_Risk_Obesity = 0; BMI_Status_Low_Risk_Obesity = 0; BMI_Status_Moderate_Risk_Obesity = 0; BMI_Status_Overweight = 0; BMI_Status_Underweight = 1
    elif (round(BMI,1) >= 18.5) &  (round(BMI,1) <= 24.9):
        BMI_Status_High_Risk_Obesity = 0; BMI_Status_Low_Risk_Obesity = 0; BMI_Status_Moderate_Risk_Obesity = 0; BMI_Status_Overweight = 0; BMI_Status_Underweight = 0
    elif (round(BMI,1) >= 25.0) &  (round(BMI,1) <= 29.9):
        BMI_Status_High_Risk_Obesity = 0; BMI_Status_Low_Risk_Obesity = 0; BMI_Status_Moderate_Risk_Obesity = 0; BMI_Status_Overweight = 1; BMI_Status_Underweight = 0
    elif (round(BMI,1) >= 30.0) &  (round(BMI,1) <= 34.9):
        BMI_Status_High_Risk_Obesity = 0; BMI_Status_Low_Risk_Obesity = 1; BMI_Status_Moderate_Risk_Obesity = 0; BMI_Status_Overweight = 0; BMI_Status_Underweight = 0
    elif (round(BMI,1) >= 35.0) &  (round(BMI,1) <= 39.9):
        BMI_Status_High_Risk_Obesity = 0; BMI_Status_Low_Risk_Obesity = 0; BMI_Status_Moderate_Risk_Obesity = 1; BMI_Status_Overweight = 0; BMI_Status_Underweight = 0
    elif round(BMI,1) >= 39.9:
        BMI_Status_High_Risk_Obesity = 1; BMI_Status_Low_Risk_Obesity = 0; BMI_Status_Moderate_Risk_Obesity = 0; BMI_Status_Overweight = 0; BMI_Status_Underweight = 0


    diagnosis = ''
    
    if st.button('Hypertension Test Result'):
        diagnosis = hyper_prediction([BMI,
                                     PhysicalHealth,
                                     MentalHealth,
                                     SleepTime,
                                     Smoking_Yes,
                                     AlcoholDrinking_Yes,
                                     Stroke_Yes,
                                     DiffWalking_Yes,
                                     Sex_Male,
                                     AgeCategory_25_29,
                                     AgeCategory_30_34,
                                     AgeCategory_35_39,
                                     AgeCategory_40_44,
                                     AgeCategory_45_49,
                                     AgeCategory_50_54,
                                     AgeCategory_55_59,
                                     AgeCategory_60_64,
                                     AgeCategory_65_69,
                                     AgeCategory_70_74,
                                     AgeCategory_75_79,
                                     AgeCategory_80_or_older,
                                     Diabetic_No_borderline_diabetes,
                                     Diabetic_Yes,
                                     Diabetic_Yes_during_pregnancy,
                                     PhysicalActivity_Yes,
                                     GenHealth_Fair,
                                     GenHealth_Good,
                                     GenHealth_Poor,
                                     GenHealth_Very_good,
                                     Asthma_Yes,
                                     KidneyDisease_Yes,
                                     SkinCancer_Yes,
                                     Tribe_Ibibio,
                                     Tribe_Igbo,
                                     Tribe_Other,
                                     Tribe_Tiv,
                                     Tribe_Yoruba,
                                     BMI_Status_High_Risk_Obesity,
                                     BMI_Status_Low_Risk_Obesity,
                                     BMI_Status_Moderate_Risk_Obesity,
                                     BMI_Status_Overweight,
                                     BMI_Status_Underweight])
        
    
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()

 
