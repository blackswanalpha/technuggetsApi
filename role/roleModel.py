from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'role'

    id = Column("role_id",  Integer, primary_key=True, index=True)
    name = Column("role_name", String)
