from typing import List
from fastapi import Depends, APIRouter, HTTPException, Request

from sqlalchemy.orm import Session
from app.settings.database import get_db

from app.schemas.connection import SchemaConnection, ConnectionCreate, ConnectionPut
from app.settings.controller import ControllerConnection

router = APIRouter()


@router.get("/connections/", response_model=List[SchemaConnection])
def get_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = ControllerConnection(db=db)
    params = request.query_params._dict

    lpop = ["limit", "skip"]
    for param in lpop:
        if params.get(param):
            params.pop(param)

    return query.get_by(params=params, skip=skip, limit=limit)


@router.get("/connections/{model_id}", response_model=SchemaConnection)
def get(model_id: int, db: Session = Depends(get_db)):
    query = ControllerConnection(db=db)
    db_data = query.get(model_id=model_id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="Connection not found")
    return db_data


@router.put("/connections/{model_id}", response_model=SchemaConnection)
def put_by_id(model_id: int, item: ConnectionPut, db: Session = Depends(get_db)):
    query = ControllerConnection(db=db)
    return query.put(data=item.dict(), model_id=model_id)


@router.put("/connections/", response_model=SchemaConnection)
def put_by_param(request: Request, item: ConnectionPut, db: Session = Depends(get_db)):
    query = ControllerConnection(db=db)
    params = request.query_params._dict
    return query.put(data=item.dict(), params=params)


@router.post("/connections/", response_model=SchemaConnection)
def post(item: ConnectionCreate, db: Session = Depends(get_db)):
    query = ControllerConnection(db=db)
    return query.post(data=item.dict())
