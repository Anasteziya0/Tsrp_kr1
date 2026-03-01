from fastapi import FastAPI
from models import User

app = FastAPI()

user = User(name="Анастасия Данилова", id=1)

@app.get("/users")
def get_user():
    return user