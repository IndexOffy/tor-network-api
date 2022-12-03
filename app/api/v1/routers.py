from fastapi import APIRouter
from app.api.v1.endpoints import link, subpage, connection, url

router = APIRouter()
router.include_router(link.router, tags=["Links"])
router.include_router(subpage.router, tags=["SubPages"])
router.include_router(connection.router, tags=["Connection"])
router.include_router(url.router, tags=["URL"])
