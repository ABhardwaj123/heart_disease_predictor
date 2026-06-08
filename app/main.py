from fastapi import FastAPI
from app.schema import PatientData
from app.predictor import prediction
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #allows requests from any origin
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
def home():
    return {"status": "ok"}


#we take entire pydantic model in fxn definition and pass it to fxn
#fastAPI handles the unpacking , validation and passing to fxn

@app.post("/predict")
def predictHealth(data: PatientData):
    return prediction(data)
    