from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT, TEXT

from datetime import datetime
from app.core.database import Base


class Pages(Base):

    __tablename__ = "pages"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(150), unique=True, index=True)
    title = Column(String(255))
    author = Column(String(100))
    source = Column(LONGTEXT)
    keywords = Column(TEXT)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now)
