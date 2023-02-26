from fastapi import FastAPI
from mangum import Mangum

from app import __version__
from app.api.v1.routers import router
from app.core.settings import set_up


config = set_up()
app = FastAPI(
    title="TorNetwork API",
    description="TorNetwork Project API",
    version=__version__,
    root_path=config.get("ENVIRONMENT"),
)


@app.get("/status", include_in_schema=False)
def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's alive"})


@app.get("/error", include_in_schema=False)
def get_status():
    """Get error of messaging server."""
    raise


app.include_router(router, prefix="/v1")
handler = Mangum(app)
