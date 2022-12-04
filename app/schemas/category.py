from typing import Optional
from pydantic import BaseModel


class SchemaBase(BaseModel):
    reference: Optional[int] = None
    name: Optional[str] = None


class SchemaPut(SchemaBase):
    reference: Optional[int] = None
    name: Optional[str] = None


class SchemaCreate(SchemaBase):
    pass


class Schema(SchemaBase):
    id: int

    class Config:
        orm_mode = True
