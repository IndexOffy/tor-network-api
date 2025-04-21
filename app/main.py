from os import path

from fastapi import FastAPI, Depends
from mangum import Mangum

from app import __version__

from app.api.auth import auth
from app.api.v1.routers import router as router_v1
from app.api.v2.routers import router as router_v2

from app.core.security import authorization


app = FastAPI(
    title="TorNetwork API",
    description="TorNetwork Project API",
    root_path=path.abspath(path.dirname(__file__)),
    version=__version__,
    docs_url=None,
    redoc_url=None,
)


@app.get("/status", include_in_schema=False)
def get_status(user=Depends(authorization)):
    """Get status of messaging server."""
    return {"status": "it's alive"}


app.include_router(auth, prefix="/auth")

app.include_router(router_v1, prefix="/v1")
app.include_router(router_v2, prefix="/v2")

handler = Mangum(app)
