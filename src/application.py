from fastapi import FastAPI
from .api.answers_controller import router as answers_router

app = FastAPI()

app.include_router(answers_router)
