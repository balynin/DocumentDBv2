from celery import Celery
from PIL import Image
import pytesseract
from bson.objectid import ObjectId
from database import documents_collection

BROKER_URL = "amqp://localhost"
BACKEND_URL = 'mongodb://localhost:27017/documents'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

# app.conf.broker_connection_retry_on_startup = True
# app.conf.result_backend = 'rpc://'
# app.conf.task_serializer = 'json'
# app.conf.result_serializer = 'json'
# app.conf.accept_content = ['json']


@app.task
def text_recognize():
    #document = documents_collection.find_one({"_id": ObjectId(id)})
    text: object = pytesseract.image_to_string(Image.open('./uploads/789.png'))
    sub_id = "123456789hh"
    return {
        "sub_id": sub_id,
        "text": text
    }


