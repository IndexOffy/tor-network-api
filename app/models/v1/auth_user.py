from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, String, Integer
from app.core.database import Base


class AuthUser(Base):
    """Model Auth User"""

    __tablename__ = "auth_user"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(75), unique=True)
    username = Column(String(45), unique=True)
    password = Column(String(100), unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
