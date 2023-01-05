import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
# from .utils.spa_staticfiles import SPAStaticFiles # For StaticFiles for SPA (React, Vue, etc.)
from .schemas import ItemCreate


from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud
from .import models
from .import schemas
from .database import SessionLocal, engine
from graphviz import Digraph
import json
from fastapi.responses import FileResponse
from .functioins import temp
app = FastAPI()


async def get_db():
    async with SessionLocal() as db:
        yield db


@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        # Create DB tables.
        await conn.run_sync(models.Base.metadata.create_all)


@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = await crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken.")
    return await crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = await crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
async def create_sentence_for_user(
        user_id: int, sentence: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return await crud.create_user_sentence(db=db, sentence=sentence, user_id=user_id)


@app.get("/users/sentences/{user_id}", response_model=schemas.User)
async def read_sentences(user_id: int, db: Session = Depends(get_db)):
    sentences = await crud.get_sentences(db=db, user_id=user_id)
    print(sentences)
    return await crud.get_user(db, user_id=user_id)


@app.get("/users/markovchain/{user_id}")
async def generate_chain(user_id: int, db: Session = Depends(get_db)):
    sentences = await crud.get_sentences(db=db, user_id=user_id)
    edges_json = await asyncio.to_thread(temp, sentences, user_id)
    return {str(user_id): json.dumps(edges_json)}


@app.get("/image/{user_id}")
async def get_image(user_id: int):
    return FileResponse(f"markov{user_id}.png")


app.mount("", StaticFiles(directory="static_files",
          html=True), name="static_files")

# app.mount("", SPAStaticFiles(directory="static_files"), name="static_files")
