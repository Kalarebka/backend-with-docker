from motor import motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017" # here connect somehow to the other container

client = motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.data

user_collection = database.get_collection("user_collection")

post_collection = database.get_collection("post_collection")
