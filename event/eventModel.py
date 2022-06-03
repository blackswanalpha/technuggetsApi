from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy_utils import EmailType,URLType
from sqlalchemy.orm import relationship


class Event(Base):
    __tablename__ = 'events'

    id = Column("event_id",  Integer, primary_key=True, index=True)
    img  =  Column("event_img", URLType)
    name = Column("event_name", String)
    desc = Column("event_desc", String)
    link= Column("event_link", String)
    venue = Column("event_venue", String)
    speaker = Column("event_speaker", String)
    price=Column("event_price", Integer)