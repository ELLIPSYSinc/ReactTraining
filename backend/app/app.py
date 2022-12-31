from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
# from .utils.spa_staticfiles import SPAStaticFiles # For StaticFiles for SPA (React, Vue, etc.)
from .schemas import ItemCreate


app = FastAPI()


db_items = {
    1: {"item_id": 1, "text": "item1"},
    2: {"item_id": 2, "text": "item2"}
}


@app.get("/api/v1/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/items/{item_id}")
def read_item(item_id: int):
    try:
        return db_items[item_id]
    except KeyError:
        raise HTTPException(404, "Not Found")


@app.post("/api/v1/items")
def post_item(item: ItemCreate):
    new_item = {"item_id": max(db_items) + 1, "text": item.text}
    db_items[new_item["item_id"]] = new_item
    return new_item


app.mount("", StaticFiles(directory="static_files",
          html=True), name="static_files")

# app.mount("", SPAStaticFiles(directory="static_files"), name="static_files")
