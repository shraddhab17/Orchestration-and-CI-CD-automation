import uvicorn
from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

# Load the phishing detection model from a joblib file
phishing_model = open('phishing.pkl', 'rb')
phishing_model_ls = joblib.load(phishing_model)

# Define a Pydantic model for the input features
class InputFeatures(BaseModel):
    feature: str

# Endpoint for phishing prediction
@app.get('/predict/')
async def predict(features: str):
    # Make a prediction based on the provided feature
    X_predict = [features]
    y_Predict = phishing_model_ls.predict(X_predict)
    
    # Determine the result message based on the prediction
    result = "This is a Phishing Site" if y_Predict == 'bad' else "This is not a Phishing Site"

    return {'input_feature': features, 'result': result}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
