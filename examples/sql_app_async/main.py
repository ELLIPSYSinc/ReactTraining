# This example based on https://fastapi.tiangolo.com/ja/tutorial/sql-databases/

# You can run it with Uvicorn
# cd examples/sql_app_async
# python main.py

# Access http://localhost:8000/docs from browser after starting the server.

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.app:app", reload=True, reload_dirs=["./app"]
    )
