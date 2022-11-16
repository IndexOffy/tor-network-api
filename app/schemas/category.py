from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: Optional[str] = None

class CategoryPut(CategoryBase):
    name: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass


class SchemaCategory(CategoryBase):
    id: int

    class Config:
        orm_mode = True
