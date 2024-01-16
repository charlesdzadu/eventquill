from pymongo import MongoClient

from app.core.config import envSettings

client = MongoClient(envSettings.MONGO_URI)

app_db = client[envSettings.MONGO_DB_NAME]
