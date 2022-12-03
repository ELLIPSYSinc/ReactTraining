# See https://docs.sqlalchemy.org/en/14/changelog/migration_20.html#migration-orm-usage
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import models, schemas


async def get_user(db: AsyncSession, user_id: int) -> models.User | None:
    return (await db.scalars(select(models.User).where(models.User.id == user_id))).first()


async def get_user_by_email(db: AsyncSession, email: str) -> models.User | None:
    return (await db.scalars(select(models.User).where(models.User.email == email))).first()


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[models.User]:
    return (await db.scalars(select(models.User).offset(skip).limit(limit))).all()


async def create_user(db: AsyncSession, user: schemas.UserCreate) -> models.User:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email, hashed_password=fake_hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_items(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[models.Item]:
    return (await db.scalars(select(models.Item).offset(skip).limit(limit))).all()


async def create_user_item(db: AsyncSession, item: schemas.ItemCreate, user_id: int) -> models.Item:
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item
