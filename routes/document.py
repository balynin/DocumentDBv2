from fastapi import APIRouter, Body, UploadFile, HTTPException, File
import os, shutil, time

from database import add_document, delete_document, retrieve_document, retrieve_documents, update_document, documents_collection
from models.document import ErrorResponseModel, ResponseModel, DocumentSchema, UpdateDocumentModel

router = APIRouter()

@router.get("/", response_description="Documents retrieved")
async def get_students():
    documents = await retrieve_documents()
    if documents:
        return ResponseModel(documents, "Documents data retrieved successfully")
    return ResponseModel(documents, "Empty list returned")


@router.get("/{id}", response_description="Document data retrieved")
async def get_student_data(id):
    student = await retrieve_document(id)
    if student:
        return ResponseModel(student, "Document data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Document doesn't exist.")

from tasks import text_recognize
@router.get('/analyze/')
async def analyze_document():
    await text_recognize.delay()


@router.delete("/{id}", response_description="Document data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_document(id)
    if deleted_student:
        return ResponseModel(
            "Document with ID: {} removed".format(id), "Document deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Document with id {0} doesn't exist".format(id)
    )


@router.post("/", response_description="Document data added into the database")
async def document_upload(file: UploadFile = File(...)):
    file.file.seek(0, 2)
    file_size = file.file.tell()
    await file.seek(0)

    if file_size > 2 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")

    content_type = file.content_type
    if content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    UPLOAD_DIRECTORY = "./uploads"
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    now = time.time()
    document_data: dict = {
                "pic_name": file.filename,
                "date": now,
                "recognized_text": "not recognized yet",
            }
    document = await documents_collection.insert_one(document_data)
    return {"filename": file.filename}


