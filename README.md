## Heart Disease Predictor

A full end-to-end machine learning project that predicts whether a person has heart disease based on clinical features. The model returns a prediction (yes/no) along with a confidence probability


## Live Demo Link

- Frontend: https://luminous-llama-a30e09.netlify.app
- API Docs: https://heart-disease-predictor-a1n0.onrender.com/docs



## Tech Stack

- ML: scikit-learn, pandas, numpy
- Backend: Python, FastAPI, uvicorn
- Frontend: HTML, CSS, JavaScript
- Deployment: Render (backend), Netlify (frontend)



## Model Comparision between logistic regression and random forest for our model on same dataset

    Metric                  Logistic Regression         Random Forest
    
    Accuracy                       80.3%                     83.6%

    Precision                      76.9%                     78%

    Recall                         90.9%                     96.9%

    F1                             83.3%                     86.5%

    AUC                            0.87                      0.91




## Project Structure
/app
    main.py -> defining FastAPI app and endpoints
    predictor.py -> functionality of /predict endpoint
    schema.py -> Pydantic model(tells us the shape of data coming through API)

/frontend
    index.html
    style.css
    app.js -> fetch call to API and result display

/model
    rf_model.joblib -> trained random forest model
    scaler.joblib -> Fitted StandardScaler for preprocessing

/notebooks
    eda_and_training_ipynb
    heart.csv

DockerFile -> specifying requirements for container



## What I did
- Built and evaluated ML classification models using scikit-learn
- Understood that recall matters more than accuracy in medical predictions
- Served a trained model using FastAPI
- Load models with joblib for production use
- Wrote a DockerFile



Saved all of my personal new learnings in learnings.txt
