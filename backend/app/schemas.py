from pydantic import BaseModel


class ItemCreate(BaseModel):
    text: str
