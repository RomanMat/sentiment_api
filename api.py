from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from scraper import fetch_reviews
from sentiment_analyser import analyse

app = FastAPI()


class Business(BaseModel):
    Location: str
    Name: str


class Message(BaseModel):
    Text: str


@app.get("/api/")
async def analyse_default():
    """Analyse sentiment of last 10 reviews of Meat and Greet cafe in Prague."""

    reviews = fetch_reviews()
    reviews["sentiment"] = reviews["reviews"].apply(lambda x: analyse(x[:512]))
    return reviews.to_json()


@app.post("/api/analyse")
async def analyse_message(message: Message):
    """Analyse sentiment of given message."""

    sentiment_score = analyse(message.Text)
    return {"message": message.Text, "sentiment_score": sentiment_score}


@app.post("/api/yelp")
async def analyse_business(business_props: Business):
    """Analyse sentiment of 10 last reviews of given business if exists at Yelp."""

    try:
        reviews = fetch_reviews(
            location=business_props.Location, name=business_props.Name
        )
    except ValueError:
        raise HTTPException(status_code=404, detail="Business not found")

    reviews["sentiment"] = reviews["reviews"].apply(lambda x: analyse(x[:512]))

    reviews = reviews.to_dict()
    reviews["business"] = business_props.Name
    reviews["location"] = business_props.Location

    return reviews
