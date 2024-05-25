import motor.motor_asyncio
from pymongo import MongoClient
from bson.objectid import ObjectId

# асинхронный драйвер к МонгоДБ
client = motor.motor_asyncio.AsyncIOMotorClient("mongo://root:example@mongo:27017")
database = client.documents
documents_collection = database.get_collection("documents_collection")
# Синхронный драйвер к МонгоДБ
client = MongoClient("mongodb://root:example@mongo:27017/")
db = client.documents
collection = db.documents_collection



def document_helper(document) -> dict:
    return {
        "id": str(document["_id"]),
        "pic_name": document["pic_name"],
        "date": document["date"],
        "recognized_text": document["recognized_text"]
    }


async def retrieve_documents():
    documents = []
    async for document in documents_collection.find():
        documents.append(document_helper(document))
    return documents


async def add_document(document_data: dict) -> dict:
    document = await documents_collection.insert_one(document_data)
    new_document = await documents_collection.find_one({"_id": document.inserted_id})
    return document_data(new_document)


async def retrieve_document(id: str) -> dict:
    document = await documents_collection.find_one({"_id": ObjectId(id)})
    if document:
        return document_helper(document)


async def delete_document(id: str):
    document = await documents_collection.find_one({"_id": ObjectId(id)})
    if document:
        await documents_collection.delete_one({"_id": ObjectId(id)})
        return True
