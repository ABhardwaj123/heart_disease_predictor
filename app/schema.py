from pydantic import BaseModel

#this schema.py has the shape of data coming through API
class PatientData(BaseModel):
    age: int      
    sex: int  
    cp: int  
    trestbps: int  
    chol: int         
    fbs: int  
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int  
    thal: int
