import motor.motor_asyncio
import os

from fastapi import FastAPI
from . import models

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client["fastapi"]

@app.get("/")
async def index():
    return {"the app": "it's alive!!!"}

@app.get("/get-mongo-users")
async def get_mongo_stuff():
    users = await db["users"].find({}, {"_id": 0}).to_list(10)
    return users

@app.get("/get-mongo-posts")
async def get_mongo_posts():
    posts = await db["posts"].find({}, {"_id": 0}).to_list(10)
    return posts
