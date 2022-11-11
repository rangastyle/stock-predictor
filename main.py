#Install dependencies
#python -m pip install -U -q fastapi uvicorn
#pip install -U -q fastapi uvicorn

# create a new instance of FastAPI and set up a quick test route
from fastapi import FastAPI
app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}


from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from model import predict, convert

app = FastAPI()

# pydantic models
class StockIn(BaseModel):
    ticker: str
    days: int

class StockOut(StockIn):
    forecast: dict

@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    ticker = payload.ticker
    days = payload.days

    prediction_list = predict(ticker, days)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "ticker": ticker, 
        "days": days,
        "forecast": convert(prediction_list)}
    return response_object