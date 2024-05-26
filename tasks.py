from celery import Celery
from PIL import Image
import pytesseract
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin_password@db:27017/")
db = client.documents
collection = db.documents_collection

BROKER_URL: str = "redis://redis:6379"
BACKEND_URL: str = 'redis://redis:6379'
# CELERY_BROKER_URL = 'redis://redis:6379'
# CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_task_store_errors_even_if_ignored = True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True


app = Celery('tasks', broker=BROKER_URL,
             backend=BACKEND_URL,
             serializer=CELERY_RESULT_SERIALIZER,
             task_serializer=CELERY_TASK_SERIALIZER,
             task_store_errors_even_if_ignored=CELERY_task_store_errors_even_if_ignored,
             BROKER_CONNECTION_RETRY_ON_STARTUP=CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP
)


@app.task
def text_recognize(id):
    document = collection.find_one({"_id": ObjectId(id)})
    sub_id = document['_id']
    pic_name = document['pic_name']
    text: str = pytesseract.image_to_string(Image.open('./uploads/' + pic_name))

    return text


