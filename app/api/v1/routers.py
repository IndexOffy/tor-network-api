from fastapi import APIRouter
from app.api.v1.endpoints import link, subpage

router = APIRouter()
router.include_router(link.router, tags=["Links"])
router.include_router(subpage.router, tags=["SubPages"])