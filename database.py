import motor.motor_asyncio
from bson.objectid import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.documents
documents_collection = database.get_collection("documents_collection")


# helpers

def document_helper(document) -> dict:
    return {
        "id": str(document["_id"]),
        "pic_name": document["pic_name"],
        "date": document["date"],
        "recognized_text": document["recognized_text"],
    }


async def retrieve_documents():
    documents = []
    async for document in documents_collection.find():
        documents.append(document_helper(document))
    return documents


# Add a new student into to the database
async def add_document(document_data: dict) -> dict:
    document = await documents_collection.insert_one(document_data)
    new_document = await documents_collection.find_one({"_id": document.inserted_id})
    return document_data(new_document)


# Retrieve a student with a matching ID
async def retrieve_document(id: str) -> dict:
    document = await documents_collection.find_one({"_id": ObjectId(id)})
    if document:
        return document_helper(document)


# async def update_document(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     document = await documents_collection.find_one({"_id": ObjectId(id)})
#     if document:
#         updated_document = await documents_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_document:
#             return True
#         return False
#

async def delete_document(id: str):
    document = await documents_collection.find_one({"_id": ObjectId(id)})
    if document:
        await documents_collection.delete_one({"_id": ObjectId(id)})
        return True
