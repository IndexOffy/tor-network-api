from fastapi import FastAPI
from app.api.v1.routers import router


app = FastAPI(
    title="OnionAPI",
    description="Project OnionAPI",
    version="0.0.1"
)

app.include_router(router, prefix="/v1")
