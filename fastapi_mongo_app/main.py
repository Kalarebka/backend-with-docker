import motor.motor_asyncio
import os

from fastapi import FastAPI

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.college

@app.get("/")
async def index():
    return {"the app": "it's alive!!!"}

@app.get("/get-mongo-stuff")
async def get_mongo_stuff():
    pass


from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    

class Post(BaseModel):
    title: str
    content: str
