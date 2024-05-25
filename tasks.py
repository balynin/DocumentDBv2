from celery import Celery
from PIL import Image
import pytesseract
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://root:example@mongo:27017/")
db = client.documents
collection = db.documents_collection

BROKER_URL: str = "redis://redis:6379"
BACKEND_URL: str = 'redis://redis:6379'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

@app.task
def text_recognize(id):
    document = collection.find_one({"_id": ObjectId(id)})
    sub_id = document['_id']
    pic_name = document['pic_name']
    text: str = pytesseract.image_to_string(Image.open('./uploads/' + pic_name))

    return text


