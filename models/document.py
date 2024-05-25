from typing import Optional
from pydantic import BaseModel, Field


class DocumentSchema(BaseModel):
    pic_name: str = Field(...)
    date: str = Field(...)
    recognized_text: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "pic_name": "test.jpg",
                "date": "1716295282.847",
                "recognized_text": "not recognized yet"
            }
        }


class UpdateDocumentModel(BaseModel):
    pic_name: Optional[str]
    date: Optional[str]
    recognized_text: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "pic_name": "test.jpg",
                "date": "1716295282.847",
                "recognized_text": "not recognized yet"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
