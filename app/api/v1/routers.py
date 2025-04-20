from fastapi import APIRouter
from app.api.v1.endpoints import link, connection, category, subpage, url

router = APIRouter()
router.include_router(link.router, tags=["Links"])
router.include_router(connection.router, tags=["LinkConnection"])
router.include_router(category.router, tags=["Category"])
router.include_router(subpage.router, tags=["SubPages"])
router.include_router(url.router, tags=["URL"])
