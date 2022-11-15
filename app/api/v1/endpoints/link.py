from typing import List
from fastapi import Depends, APIRouter, HTTPException, Request

from sqlalchemy.orm import Session
from app.settings.database import get_db

from app.schemas.link import SchemaLink, LinkCreate, LinkPut
from app.settings.controller import ControllerLink

router = APIRouter()


@router.get("/links/", response_model=List[SchemaLink])
def get_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = ControllerLink(db=db)
    params = request.query_params._dict
    if params:
        return query.get_by(params=params)
    return query.all(skip=skip, limit=limit)


@router.get("/links/{model_id}", response_model=SchemaLink)
def get(model_id: int, db: Session = Depends(get_db)):
    query = ControllerLink(db=db)
    db_data = query.get(model_id=model_id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_data


@router.put("/links/{model_id}", response_model=SchemaLink)
def put_by_id(model_id: int, item: LinkPut, db: Session = Depends(get_db)):
    query = ControllerLink(db=db)
    return query.put(data=item.dict(), model_id=model_id)


@router.put("/links/", response_model=SchemaLink)
def put_by_param(request: Request, item: LinkPut, db: Session = Depends(get_db)):
    query = ControllerLink(db=db)
    params = request.query_params._dict
    return query.put(data=item.dict(), params=params)


@router.post("/links/", response_model=SchemaLink)
def post(item: LinkCreate, db: Session = Depends(get_db)):
    query = ControllerLink(db=db)
    return query.post(data=item.dict())
