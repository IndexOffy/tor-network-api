from typing import Optional
from pydantic import BaseModel


class ConnectionBase(BaseModel):
    title: Optional[int] = None
    id_link: Optional[int] = None
    id_href: Optional[int] = None
    status: Optional[bool] = None


class ConnectionPut(ConnectionBase):
    title: Optional[int] = None
    id_link: Optional[int] = None
    id_href: Optional[int] = None
    status: Optional[bool] = None


class ConnectionCreate(ConnectionBase):
    pass


class SchemaConnection(ConnectionBase):
    id: int

    class Config:
        orm_mode = True
