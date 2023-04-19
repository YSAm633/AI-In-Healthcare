import numpy as np
import pandas as pd
import sklearn
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk
from tkinter import ttk

# Define a list of diseases and conditions
diseases = ['Healthy', 'Hypertension', 'Diabetes', 'Obesity', 'Hyperthyroidism', 'Hypothyroidism']

# Define a function to get the diagnosis
def get_diagnosis():
    # Get input data from user
    age = float(age_entry.get())
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    systolic_bp = float(systolic_bp_entry.get())
    diastolic_bp = float(diastolic_bp_entry.get())
    cholesterol = float(cholesterol_entry.get())
    glucose = float(glucose_entry.get())

    # Use the model to make a prediction on the user's data
    X_new = np.array([age, height, weight, systolic_bp, diastolic_bp, cholesterol, glucose]).reshape(1, -1)
    y_pred = model.predict(X_new)

    # Print the predicted diagnosis or disease
    if y_pred == 0:
        diagnosis_label.config(text="You are healthy.")
    else:
        diagnosis_label.config(text="You may have " + diseases[int(y_pred)] + " and should seek medical attention.")

# Prepare the data
data = np.array([[40, 1.6, 70, 110, 70, 80, 1.0, 0], 
                 [50, 1.8, 90, 120, 80, 85, 1.2, 1],
                 [35, 1.7, 65, 100, 60, 75, 0.8, 0],
                 [55, 1.65, 75, 130, 90, 90, 1.3, 2],
                 [45, 1.75, 80, 120, 80, 85, 1.2, 1],
                 [30, 1.5, 50, 90, 60, 70, 0.9, 2]])

df = pd.DataFrame(data, columns=['age', 'height', 'weight', 'systolic_bp', 'diastolic_bp', 'cholesterol', 'glucose', 'diagnosis'])

# Prepare the data for training
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

# Train a machine learning model on the data
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Create GUI
root = tk.Tk()
root.title("Health Diagnosis")

# Create labels and entries
age_label = ttk.Label(root, text="Age:")
age_entry = ttk.Entry(root)

height_label = ttk.Label(root, text="Height (in meters):")
height_entry = ttk.Entry(root)

weight_label = ttk.Label(root, text="Weight (in kilograms):")
weight_entry = ttk.Entry(root)

systolic_bp_label = ttk.Label(root, text="Systolic blood pressure:")
systolic_bp_entry = ttk.Entry(root)

diastolic_bp_label = ttk.Label(root, text="Diastolic blood pressure:")
diastolic_bp_entry = ttk.Entry(root)

cholesterol_label = ttk.Label(root, text="Cholesterol level:")
cholesterol_entry = ttk.Entry(root)

glucose_label = ttk.Label(root, text="Glucose level:")
glucose_entry = ttk.Entry(root)

# Create button
#Create button to get diagnosis
diagnosis_button = ttk.Button(root, text="Get Diagnosis", command=get_diagnosis)

#Create label for diagnosis
diagnosis_label = ttk.Label(root, text="")

#Place labels and entries on the grid
age_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")
age_entry.grid(row=0, column=1, padx=5, pady=5)

height_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
height_entry.grid(row=1, column=1, padx=5, pady=5)

weight_label.grid(row=2, column=0, padx=5, pady=5, sticky="W")
weight_entry.grid(row=2, column=1, padx=5, pady=5)

systolic_bp_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")
systolic_bp_entry.grid(row=3, column=1, padx=5, pady=5)

diastolic_bp_label.grid(row=4, column=0, padx=5, pady=5, sticky="W")
diastolic_bp_entry.grid(row=4, column=1, padx=5, pady=5)

cholesterol_label.grid(row=5, column=0, padx=5, pady=5, sticky="W")
cholesterol_entry.grid(row=5, column=1, padx=5, pady=5)

glucose_label.grid(row=6, column=0, padx=5, pady=5, sticky="W")
glucose_entry.grid(row=6, column=1, padx=5, pady=5)

#Place button and label on the grid
diagnosis_button.grid(row=7, column=1, padx=5, pady=5, sticky="E")
diagnosis_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

#Start the GUI
root.mainloop()