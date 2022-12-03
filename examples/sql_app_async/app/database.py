from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import cast, Callable, AsyncContextManager

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./db/sql_app.db"

# See https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#synopsis-orm
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = cast(
    Callable[[], AsyncContextManager[AsyncSession]],
    sessionmaker(
        engine, expire_on_commit=False, autocommit=False, autoflush=False, class_=AsyncSession
    )
)

Base = declarative_base()
