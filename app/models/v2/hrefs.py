from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT

from datetime import datetime
from app.core.database import Base


class Hrefs(Base):

    __tablename__ = "hrefs"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(150), unique=True, index=True)
    source = Column(LONGTEXT)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now)
