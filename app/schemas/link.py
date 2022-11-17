from typing import Optional
from pydantic import BaseModel


class LinkBase(BaseModel):
    link: str
    title: Optional[str] = None
    author: Optional[str] = None
    keywords: Optional[str] = None
    verify: Optional[bool] = None
    explored: Optional[bool] = None
    running: Optional[bool] = None
    fail: Optional[bool] = None
    login: Optional[bool] = None
    attempts: Optional[int] = None


class LinkCreate(LinkBase):
    pass


class LinkPut(LinkBase):
    link: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    keywords: Optional[str] = None
    verify: Optional[bool] = None
    explored: Optional[bool] = None
    running: Optional[bool] = None
    fail: Optional[bool] = None
    login: Optional[bool] = None
    attempts: Optional[int] = None


class SchemaLink(LinkBase):
    id: int

    class Config:
        orm_mode = True
