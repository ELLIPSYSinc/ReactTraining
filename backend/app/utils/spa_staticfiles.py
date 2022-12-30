from fastapi.staticfiles import StaticFiles
from starlette.types import Scope
from starlette.exceptions import HTTPException
from starlette.responses import Response


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope: Scope) -> Response:
        try:
            return await super().get_response(path, scope)
        except HTTPException as e:
            if e.status_code == 404:
                return await super().get_response("index.html", scope)
            raise e
