from os import name
from fastapi import FastAPI
from fastapi import templating
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
from db import USERS_DB

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class Notification(BaseModel):
    author: str
    description: str
    
class User(BaseModel):
    name: str
    username: str
    email: str
    birthday: str
    friends: List[str]
    notifications: List[Notification]
    
class UserDb(User):
    hashed_password: str
    

@app.get("/")
def test():
    return {"1": "2"}