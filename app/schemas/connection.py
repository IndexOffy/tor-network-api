from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    id_link: Optional[int] = None
    id_href: Optional[int] = None
    status: Optional[bool] = None


class SchemaPut(SchemaBase):
    id_link: Optional[int] = None
    id_href: Optional[int] = None
    status: Optional[bool] = None


class SchemaCreate(SchemaBase):
    pass


class Schema(SchemaBase):
    id: int

    class Config:
        orm_mode = True
