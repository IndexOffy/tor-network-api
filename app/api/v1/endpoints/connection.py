from typing import List
from fastapi import Depends, APIRouter, Request, status

from sqlalchemy.orm import Session
from app.core.database import get_db

from app.schemas.connection import Schema, SchemaCreate, SchemaPut
from app.core.controller import ControllerConnection as Controller


router = APIRouter()


@router.get("/connections/", response_model=List[Schema])
def get_all(
        request: Request,
        offset: int = 0,
        limit: int = 100,
        sort_by: str = 'id',
        order_by: str = 'desc',
        db: Session = Depends(get_db)):
    return Controller(db=db)._get_all(
        request=request,
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        order_by=order_by,
    )


@router.get("/connections/{model_id}", response_model=Schema)
def get_one(model_id: int, db: Session = Depends(get_db)):
    return Controller(db=db).get(model_id=model_id)


@router.put("/connections/{model_id}", response_model=Schema)
def update(model_id: int, item: SchemaPut, db: Session = Depends(get_db)):
    return Controller(db=db).put(data=item.dict(), model_id=model_id)


@router.post("/connections/", response_model=Schema, status_code=status.HTTP_201_CREATED)
def create(item: SchemaCreate, db: Session = Depends(get_db)):
    return Controller(db=db).post(data=item.dict())
