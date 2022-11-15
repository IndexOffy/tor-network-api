from sqlalchemy import Column, Integer, String
from app.settings.database import Base, engine


class Category(Base):
    __tablename__ = "category"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))


Base.metadata.create_all(bind=engine)
