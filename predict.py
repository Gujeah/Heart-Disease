import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import traceback

app = Flask(__name__)


try:
    with open("model.pkl", 'rb') as file:
        load_model = pickle.load(file)
    print("Model loaded successfully!")
    print("Pipeline steps:", load_model.named_steps) 
except Exception as e:
    print(f"Error loading model: {e}")
    load_model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if load_model is None:
            raise Exception("Model not properly loaded")

        #getting data from the form 
        user_data = {
            'age': int(request.form['age']),
            'sex': str(request.form['sex']),
            'dataset': str(request.form['dataset']),
            'cp': str(request.form['cp']),
            'trestbps': float(request.form['trestbps']),
            'chol': float(request.form['chol']),
            'fbs': int(request.form['fbs']),
            'restecg': str(request.form['restecg']),
            'thalch': float(request.form['thalch']),
            'exang': int(request.form['exang']),
            'oldpeak': float(request.form['oldpeak'])
        }
        
    
        user_df = pd.DataFrame([user_data])
        
       #Probabilities
        probabilities = load_model.predict_proba(user_df)
        positive_class_prob = probabilities[0][1]
        
       
        risk_message = (
            "High Risk of Heart Disease" 
            if positive_class_prob > 0.55 
            else "Low Risk of Heart Disease"
        )
        
       
        return render_template(
            'index.html',
            risk_message=risk_message,
            probability=f"{positive_class_prob * 100:.2f}%"
        )

    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return render_template(
            'index.html',
            risk_message="Error in prediction process",
            probability="N/A"
        )

if __name__ == "__main__":
    app.run(debug=True)