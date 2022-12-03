from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    link: str
    verify: Optional[bool] = None
    running: Optional[bool] = None
    fail: Optional[bool] = None


class SchemaCreate(SchemaBase):
    pass


class SchemaPut(SchemaBase):
    link: Optional[str] = None
    verify: Optional[bool] = None
    running: Optional[bool] = None
    fail: Optional[bool] = None


class Schema(SchemaBase):
    id: int

    class Config:
        orm_mode = True
