from sqlalchemy import Column, Integer, Boolean, UniqueConstraint, ForeignKey

from app.core.database import Base
from app.models.v2.pages import Pages


class Relationships(Base):

    __tablename__ = "relationships"
    __table_args__ = (
        UniqueConstraint(
            "id_page",
            "id_redirect",
            name="unique_component_commit"
        ),
    )

    id_page = Column(Integer, ForeignKey(Pages.id), index=True)
    id_redirect = Column(Integer, ForeignKey(Pages.id), index=True)
    status = Column(Boolean, default=True)
