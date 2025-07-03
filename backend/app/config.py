import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
events_collection = db["events"]

# Optional: Create indexes
events_collection.create_index("request_id")
events_collection.create_index("timestamp")
