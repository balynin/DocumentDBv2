from bson.objectid import ObjectId
from database import documents_collection
import json

id = '664cfa32434cc86acffb659d'
document = documents_collection.find_one({"_id": ObjectId(id)})
a_dict = document.result()
print(document.__dir__)
