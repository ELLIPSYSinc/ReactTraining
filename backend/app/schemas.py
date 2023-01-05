from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    sentence: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    sentences: List[Item] = []
    class Config:
        orm_mode = True
