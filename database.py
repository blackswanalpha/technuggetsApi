from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

SQLALCHAMY_DATABASE_URL = 'postgresql://postgres:password@localhost:5432/nuggets_db'
engine = create_engine(SQLALCHAMY_DATABASE_URL,pool_pre_ping=True,pool_recycle=300)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, )
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
