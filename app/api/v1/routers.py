from fastapi import APIRouter
from app.api.v1.endpoints import link, subpage, connection

router = APIRouter()
router.include_router(link.router, tags=["Links"])
router.include_router(subpage.router, tags=["SubPages"])
router.include_router(connection.router, tags=["Connection"])