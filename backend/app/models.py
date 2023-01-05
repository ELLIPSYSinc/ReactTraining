from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), unique=True, index=True)
    sentences = relationship("Item", back_populates="owner", lazy="selectin")


class Item(Base):
    __tablename__ = "sentences"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sentence = Column(Text, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="sentences", lazy="joined")
