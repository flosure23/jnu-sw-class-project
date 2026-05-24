from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.spam import classify_text
from app.model_loader import get_model_info


app = FastAPI(title="AI Spam Checker")


class SpamRequest(BaseModel):
    text: str


@app.post("/classify")
def classify(request: SpamRequest):
    try:
        label, score = classify_text(request.text)

        return {
            "label": label,
            "score": score,
            "model_info": get_model_info(),
            "error": None
        }

    except Exception as e:
        return {
            "label": "error",
            "score": -1,
            "model_info": get_model_info(),
            "error": str(e)
        }


app.mount("/", StaticFiles(directory="static", html=True), name="static")