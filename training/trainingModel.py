from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy_utils import EmailType,URLType
from sqlalchemy.orm import relationship


class Training(Base):
    __tablename__ = 'training'

    id = Column("training_id",  Integer, primary_key=True, index=True)
    img  =  Column("training_img", URLType)
    name = Column("training_name", String)
    desc = Column("training_desc", String)
    link= Column("training_link", String)
    location = Column("training_location", String)
    provider = Column("training_provider", String)
    fee=Column("training_fee", Integer)