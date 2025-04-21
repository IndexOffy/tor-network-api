from typing import List
from fastapi import Depends, APIRouter, Request, status

from sqlalchemy.orm import Session
from app.core.database import get_db

from app.schemas.v1.url import Schema, SchemaCreate, SchemaPut
from app.core.controller import ControllerUrl as Controller


router = APIRouter()


@router.get("/urls/", response_model=List[Schema])
def get_all(
    request: Request,
    offset: int = 0,
    limit: int = 100,
    sort_by: str = "id",
    order_by: str = "desc",
    db: Session = Depends(get_db),
):
    return Controller(db=db).read(
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        order_by=order_by,
        qtype="all",
        params=request.query_params._dict,
    )


@router.get("/urls/{model_id}", response_model=Schema)
def get_one(model_id: int, db: Session = Depends(get_db)):
    return Controller(db=db).read(qtype="first", params={"id": model_id})


@router.put("/urls/{model_id}", response_model=Schema)
def update(model_id: int, item: SchemaPut, db: Session = Depends(get_db)):
    return Controller(db=db).update(data=item.dict(), model_id=model_id)


@router.post("/urls/", response_model=Schema, status_code=status.HTTP_201_CREATED)
def create(item: SchemaCreate, db: Session = Depends(get_db)):
    return Controller(db=db).create(data=item.dict())


@router.put("/urls/", response_model=Schema, include_in_schema=False)
def put_by_param(request: Request, item: SchemaPut, db: Session = Depends(get_db)):
    query = Controller(db=db)
    params = request.query_params._dict
    return query.update(data=item.dict(), params=params)
