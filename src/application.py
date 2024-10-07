from fastapi import FastAPI # type: ignore
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from .api.answers_controller import router as answers_router

app = FastAPI()

app.include_router(answers_router)
