from sqlalchemy import Column, Integer, ForeignKey

from app.core.database import Base
from app.models import AuthUser, AuthGroup


class AuthUserGroup(Base):
    """Model Auth User Groups"""

    __tablename__ = "auth_user_groups"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(AuthUser.id))
    group_id = Column(Integer, ForeignKey(AuthGroup.id))
