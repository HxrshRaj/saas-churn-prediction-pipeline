
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"pred":0.5}
