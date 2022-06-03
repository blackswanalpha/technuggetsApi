from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy_utils import EmailType,URLType
from sqlalchemy.orm import relationship


class Job(Base):
    __tablename__ = 'jobs'

    id = Column("job_id",  Integer, primary_key=True, index=True)
    img  =  Column("job_img", URLType)
    name = Column("job_name", String)
    desc = Column("job_desc", String)
    link= Column("job_link", String)
    venue = Column("job_venue", String)
    provider = Column("job_provider", String)
    requirement=Column("job_requirement", String)