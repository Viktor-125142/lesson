from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predict/")
async def predict(item: Item):
    """Sentiment analysis for a text"""

    return classifier(item.text)[0]
