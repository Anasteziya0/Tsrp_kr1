from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from models import User, UserAge, Feedback
from typing import List

app = FastAPI()

feedbacks = []

user = User(name="Данилова Анастасия", id=1)

class Numbers(BaseModel):
    num1: float
    num2: float

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

@app.get("/users")
async def get_user():
    return user

@app.post("/user")
async def check_user(user: UserAge):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    try:
        feedbacks.append(feedback)
        return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/feedbacks")
async def get_feedbacks():
    return feedbacks