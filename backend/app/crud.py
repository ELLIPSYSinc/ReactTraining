from sqlalchemy.orm import Session
from . import models
from . import schemas
from sqlalchemy.future import select


async def get_user(db: Session, user_id: int):
    return (await db.scalars(select(models.User).where(models.User.id == user_id))).first()

async def get_sentences(db: Session,user_id: int) -> list[models.Item]:
    stmt = select(models.Item).order_by(models.Item.id).where(models.Item.owner_id == user_id)
    items: list[models.Item] = (await db.scalars(stmt)).all()
    return items

async def get_user_by_username(db: Session, username: str):
    return (await db.scalars(select(models.User).where(models.User.username == username))).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return (await db.scalars(select(models.User).offset(skip).limit(limit))).all()

async def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username = user.username)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_sentences_all(db: Session, skip: int = 0, limit: int = 100):
    return (await db.scalars(select(models.Item).offset(skip).limit(limit))).all()

async def create_user_sentence(db: Session, sentence: schemas.ItemCreate, user_id: int):
    db_sentence = models.Item(**sentence.dict(), owner_id=user_id)
    db.add(db_sentence)
    await db.commit()
    await db.refresh(db_sentence)
    return db_sentence
