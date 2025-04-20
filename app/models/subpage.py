from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.core.database import Base


class SubPage(Base):
    __tablename__ = "subpage"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String(150), unique=True, index=True)
    verify = Column(Boolean, default=False, index=True)
    running = Column(Boolean, default=False, index=True)
    fail = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
