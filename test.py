from bson.objectid import ObjectId
from database import documents_collection
import json
import  asyncio
async def sample():
    id = '664cfa32434cc86acffb659d'
    document = await documents_collection.find_one({"_id": ObjectId(id)})
#a_dict = document.result()
    print(document.__dir__)


asyncio.run(sample())