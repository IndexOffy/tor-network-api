from fastapi import APIRouter
from app.api.v1.endpoints import link

router = APIRouter()
router.include_router(link.router, tags=["Links"])