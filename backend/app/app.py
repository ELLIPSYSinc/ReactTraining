from fastapi import FastAPI
from .utils.spa_staticfiles import SPAStaticFiles


app = FastAPI()


@app.get("/api/v1/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


app.mount("", SPAStaticFiles(directory="static_files"), name="static_files")
