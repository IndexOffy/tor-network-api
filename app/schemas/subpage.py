from typing import Optional
from pydantic import BaseModel


class SubPageBase(BaseModel):
    link: str
    verify: Optional[bool] = None
    running: Optional[bool] = None
    fail: Optional[bool] = None


class SubPageCreate(SubPageBase):
    pass


class SubPagePut(SubPageBase):
    link: Optional[str] = None
    verify: Optional[bool] = None
    running: Optional[bool] = None
    fail: Optional[bool] = None


class SchemaSubPage(SubPageBase):
    id: int

    class Config:
        orm_mode = True
