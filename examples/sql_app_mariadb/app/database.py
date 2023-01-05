import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import cast, Callable, AsyncContextManager

mariadb_user: str = os.environ["MARIADB_USER"]
mariadb_password: str = os.environ["MARIADB_PASSWORD"]
mariadb_database: str = os.environ["MARIADB_DATABASE"]

SQLALCHEMY_DATABASE_URL = f"mariadb+asyncmy://{mariadb_user}:{mariadb_password}@db/{mariadb_database}?charset=utf8mb4"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=3600)
SessionLocal = cast(
    Callable[[], AsyncContextManager[AsyncSession]],
    sessionmaker(
        engine, future=True, autocommit=False, autoflush=False, class_=AsyncSession
    )
)

Base = declarative_base()
