from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Category(Base):
    __tablename__ = "category"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    reference = Column(Integer)
    name = Column(String(45))
