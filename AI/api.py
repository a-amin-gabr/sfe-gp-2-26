import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Global variable for the sentiment intensity analyzer
sia = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles startup and shutdown events.
    Downloads the VADER lexicon (extremely lightweight, ~100KB)
    and initializes the Sentiment Intensity Analyzer.
    """
    global sia
    # Download the lexicon quietly
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()
    yield
    sia = None

app = FastAPI(
    title="Sentiment Analysis API", 
    description="Lightweight Backend API for Sentiment Analysis using NLTK VADER",
    version="1.0.0",
    lifespan=lifespan
)

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float

@app.post("/predict", response_model=SentimentResponse)
async def predict_sentiment(request: SentimentRequest):
    """
    Predict the sentiment (POSITIVE or NEGATIVE) of the provided text.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    
    if sia is None:
        raise HTTPException(status_code=503, detail="Model is not loaded yet.")
    
    try:
        # Get sentiment polarity scores
        scores = sia.polarity_scores(request.text)
        compound_score = scores['compound']
        
        # Map compound score (-1.0 to 1.0) to POSITIVE/NEGATIVE with a confidence proxy
        if compound_score >= 0.05:
            sentiment = "POSITIVE"
            # Normalize compound score (0.05 to 1.0) into a [0.5, 1.0] confidence range
            confidence = 0.5 + (compound_score / 2.0)
        elif compound_score <= -0.05:
            sentiment = "NEGATIVE"
            confidence = 0.5 + (abs(compound_score) / 2.0)
        else:
            # Borderline neutral scores fallback to the sign of the compound score
            sentiment = "POSITIVE" if compound_score >= 0 else "NEGATIVE"
            confidence = 0.5
            
        return SentimentResponse(
            sentiment=sentiment,
            confidence=round(confidence, 4)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")

@app.get("/")
async def health_check():
    """
    Health check endpoint to verify that the API is up and running.
    """
    return {
        "status": "healthy",
        "model": "nltk-vader-lexicon"
    }
