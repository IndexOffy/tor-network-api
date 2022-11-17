from typing import List
from fastapi import Depends, APIRouter, HTTPException, Request

from sqlalchemy.orm import Session
from app.settings.database import get_db

from app.schemas.subpage import SchemaSubPage, SubPageCreate, SubPagePut
from app.settings.controller import ControllerSubPage

router = APIRouter()


@router.get("/subpages/", response_model=List[SchemaSubPage])
def get_all(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = ControllerSubPage(db=db)
    params = request.query_params._dict

    lpop = ["limit", "skip"]
    for param in lpop:
        if params.get(param):
            params.pop(param)

    return query.get_by(params=params, skip=skip, limit=limit)


@router.get("/subpages/{model_id}", response_model=SchemaSubPage)
def get(model_id: int, db: Session = Depends(get_db)):
    query = ControllerSubPage(db=db)
    db_data = query.get(model_id=model_id)
    if db_data is None:
        raise HTTPException(status_code=404, detail="SubPage not found")
    return db_data


@router.put("/subpages/{model_id}", response_model=SchemaSubPage)
def put_by_id(model_id: int, item: SubPagePut, db: Session = Depends(get_db)):
    query = ControllerSubPage(db=db)
    return query.put(data=item.dict(), model_id=model_id)


@router.put("/subpages/", response_model=SchemaSubPage)
def put_by_param(request: Request, item: SubPagePut, db: Session = Depends(get_db)):
    query = ControllerSubPage(db=db)
    params = request.query_params._dict
    return query.put(data=item.dict(), params=params)


@router.post("/subpages/", response_model=SchemaSubPage)
def post(item: SubPageCreate, db: Session = Depends(get_db)):
    query = ControllerSubPage(db=db)
    return query.post(data=item.dict())
