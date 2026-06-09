from app.schema import PatientData
import numpy as np
import pandas as pd
import joblib
import os

#__file__ is the path of predictor.py 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
loaded_model = joblib.load(os.path.join(BASE_DIR, "..", "model", "rf_model.joblib"))
loaded_scalar = joblib.load(os.path.join(BASE_DIR, "..", "model", "scaler.joblib"))


#only these continuous columns to be normalized
numerical_cols = ["age", "trestbps", "chol", "thalach" , "oldpeak"]


def prediction(PatientData):
    
    inputData = PatientData.dict()
    npData = pd.DataFrame([inputData])

    #transforming/normalizing the input data
    npData[numerical_cols] = loaded_scalar.transform(npData[numerical_cols])

    #output just gives 0/1
    predictedOutput = loaded_model.predict(npData)
    #probability gives inidividual probabilities of 0 and 1
    predictProba = loaded_model.predict_proba(npData)

    #we return the probability of only positive rate
    return {
        "prediction": int(predictedOutput[0]),
        "probability": float(predictProba[0][1])
    }

    