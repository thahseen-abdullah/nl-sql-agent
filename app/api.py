from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from app.agent import ask_database

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "NL-SQL Agent API is running"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        result = ask_database(request.question)
        return result

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
