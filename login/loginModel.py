from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'login'

    id = Column("login_id",  Integer, primary_key=True, index=True)
    name = Column("login_name", String)
    status = Column("login_status", Integer)
    password = Column("login_password", String)

