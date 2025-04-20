from fastapi import FastAPI, Depends
from mangum import Mangum

from app import __version__
from app.api.auth import auth
from app.api.v1.routers import router
from app.core.settings import set_up
from app.core.security import authorization


config = set_up()
app = FastAPI(
    title="TorNetwork API",
    description="TorNetwork Project API",
    root_path=config.get("ENVIRONMENT"),
    version=__version__,
    docs_url=None,
    redoc_url=None,
)


@app.get("/status", include_in_schema=False)
def get_status(user=Depends(authorization)):
    """Get status of messaging server."""
    return {"status": "it's alive"}


@app.get("/error", include_in_schema=False)
def get_error(user=Depends(authorization)):
    """Get error of messaging server."""
    raise


app.include_router(auth, prefix="/auth")
app.include_router(router, prefix="/v1")
handler = Mangum(app)
