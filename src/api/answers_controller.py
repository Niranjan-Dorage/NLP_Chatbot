from fastapi import APIRouter # type: ignore
from pydantic import BaseModel # type: ignore
import spacy # type: ignore

from ..data.faq import data as data

router = APIRouter()
nlp = spacy.load("en_core_web_sm")

class Question(BaseModel):
    question: str

@router.post("/answer")
async def answer(question: Question):
    
    doc = nlp(question.question)
    better_answer = None
    max_similarity = -1
    
    for q, a in data.items():
        similarity = doc.similarity(nlp(q))
        if similarity > max_similarity:
            max_similarity = similarity
            better_answer = a
    
    return {"answer": better_answer}