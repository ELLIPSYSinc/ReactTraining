import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:app", reload_dirs=["./app"],
                port=8000, reload=True, host="0.0.0.0")
