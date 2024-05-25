from fastapi import FastAPI
from routes.document import router as DocumentRouter


app = FastAPI()
app.include_router(DocumentRouter, tags=["Document"], prefix="/document")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "ITM sprint 9 - FastAPI!"}