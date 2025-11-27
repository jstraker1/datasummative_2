import requests
from shiny import App, ui, render, reactive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import kagglehub

# UI
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_numeric(
        id = "age_input",
        label = "age",
        value = '',
        ),
        title="User Profile", # Put keyword arguments like this after positional arguments (like those stated above)
    ),
    ui.h1("Clinical Program"),
    ui.output_text('age'),
)


# Server
def server(input,output,session):
    @output
    @render.text
    def age():
        a = input.age_input()
        return a


    @reactive.Calc
    def get_df():
        path = kagglehub.dataset_download("abdallaahmed77/healthcare-risk-factors-dataset")
        df = pd.read_csv(f"{path}/dirty_v3_path.csv")
        df.rename(columns={
        "Age": "age",
        "Gender": "gender",
        "Medical Condition": "medical_condition",
        "Glucose": "glucose",
        "Blood Pressure": "blood_pressure",
        "BMI": "bmi",
        "Oxygen Saturation": "oxygen_saturation",
        "LengthOfStay": "length_of_stay",
        "Cholesterol": "cholesterol",
        "Triglycerides": "triglycerides",
        "HbA1c": "hba1c",
        "Smoking": "smoking_status",
        "Alcohol": "alcohol_use",
        "Physical Activity": "physical_activity",
        "Diet Score": "diet_score",
        "Family History": "family_history",
        "Stress Level": "stress_level",
        "Sleep Hours": "sleep_hours"
        }, inplace=True)
        df.dropna(inplace=True)
        df.reset_index(drop=True,inplace=True)
        return df

    @reactive.Calc
    def get_answers(df):
        model = sm.df
        return model

    @output
    @render.plot
    def module_attendance():
        # Get values
        # Plot graph

        return 


app = App(app_ui,server)