from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Question(BaseModel):
    question: str


@app.post("/answer")
def answer(question: Question):
    pass