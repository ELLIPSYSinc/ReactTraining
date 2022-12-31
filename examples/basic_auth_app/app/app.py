import secrets
from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials


app = FastAPI()

security = HTTPBasic()


def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_user = b"test_user"
    correct_password = b"test_password"
    if not secrets.compare_digest(credentials.username.encode("utf8"), correct_user) \
            or not secrets.compare_digest(credentials.password.encode("utf8"), correct_password):
        raise HTTPException(401, "Unauthorized")
    return credentials


@app.get("/api/v1/hello")
def read_hello_world(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    return {"Hello": "World"}


@app.get("/api/v1/me")
def read_me(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    return {"user_id": credentials.username}


app.mount("", StaticFiles(directory="static_files",
          html=True), name="static_files")
