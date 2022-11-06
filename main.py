from fastapi import FastAP
app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}
    