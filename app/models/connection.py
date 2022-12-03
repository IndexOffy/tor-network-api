from sqlalchemy import Column, Integer, Boolean, UniqueConstraint
from app.core.database import Base, engine


class Connection(Base):
    __tablename__ = "connection"
    __table_args__ = (
        UniqueConstraint('id_link', 'id_href', name='unique_component_commit'),
    )

    id = Column(Integer, primary_key=True, index=True)
    id_link = Column(Integer, index=True)
    id_href = Column(Integer, index=True)
    status = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)
