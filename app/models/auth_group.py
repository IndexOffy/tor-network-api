from sqlalchemy import Column, String, Integer

from app.core.database import Base


class AuthGroup(Base):
    """Model Auth Group"""

    __tablename__ = "auth_group"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), unique=True)
