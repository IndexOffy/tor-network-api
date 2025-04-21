from sqlalchemy import Column, Boolean, Integer, ForeignKey

from app.core.database import Base
from app.models.v2.pages import Pages


class Process(Base):

    __tablename__ = "process"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, ForeignKey(Pages.id), primary_key=True, index=True)
    verified = Column(Boolean, default=False, index=True)
    running = Column(Boolean, default=False, index=True)
    failures = Column(Integer)
    has_login = Column(Boolean, default=False)
    has_captcha = Column(Boolean, default=False)
