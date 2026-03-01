from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int

class UserAge(BaseModel):
    name: str
    age: int