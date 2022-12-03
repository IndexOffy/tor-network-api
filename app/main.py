from fastapi import FastAPI
from mangum import Mangum

from app.api.v1.routers import router
from app.config import ENVIRONMENT, BASE_DIR


with open(f"{BASE_DIR}/docs/api.md", "r", encoding="utf-8") as fh:
    description = fh.read()


app = FastAPI(
    title="TorNetwork API",
    version="0.0.1",
    description=description,
    root_path=ENVIRONMENT
)


@app.get("/status")
def get_status():
    """Get status of messaging server."""
    return ({"status": "it's alive"})


app.include_router(router, prefix="/v1")
handler = Mangum(app)
