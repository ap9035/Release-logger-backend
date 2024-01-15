from dotenv import load_dotenv
from mongoengine import Document, StringField, connect, DateTimeField
import os

load_dotenv()

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_USER = os.environ.get('MONGO_USER')
CONNECT_STRING = f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/?retryWrites=true&w=majority'

print(CONNECT_STRING)

# 建立 MongoDB 連接
connect(db="deploy-logger", host=CONNECT_STRING)


class Release(Document):
    app_name = StringField(required=True)
    version = StringField(required=True)
    update_time = DateTimeField(required=True)
