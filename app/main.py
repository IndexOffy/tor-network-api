from fastapi import FastAPI

from app.api.v1.routers import router
from app.settings.config import ENVIRONMENT
from mangum import Mangum


app = FastAPI(
    title="OnionAPI",
    description="Project OnionAPI",
    version="0.0.1",
    root_path=ENVIRONMENT
)


@app.get("/status")
def get_status():
    """Get status of messaging server."""
    return ({"status": "it's alive"})


app.include_router(router, prefix="/v1")
handler = Mangum(app)
