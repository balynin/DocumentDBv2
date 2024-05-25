from bson.objectid import ObjectId
from database import documents_collection
from pymongo import MongoClient
import  asyncio
async def sample(id):
    id = '664cfa32434cc86acffb659d'
    document = await documents_collection.find_one({"_id": ObjectId(id)})
    #a_dict = document.result()
    print(document['_id'])

id = '664cfa32434cc86acffb659d'
#asyncio.run(sample(id))

client = MongoClient("mongodb://localhost:27017/")
db = client.documents
collection = db.documents_collection

document = collection.find_one({"_id": ObjectId(id)})
print(document['_id'])


