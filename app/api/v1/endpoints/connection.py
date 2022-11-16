from typing import List
from fastapi import Depends, APIRouter, HTTPException, Request

from sqlalchemy.orm import Session
from app.settings.database import get_db

from app.schemas import SchemaConnection
from app.settings.controller import ControllerConnection

router = APIRouter()


# @router.get("/connections/", response_model=List[SchemaConnection])
# def get_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     query = ControllerLink(db=db)
#     params = request.query_params._dict
#     if params:
#         return query.get_by(params=params)
#     return query.all(skip=skip, limit=limit)