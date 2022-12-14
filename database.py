from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from bot import settings

engine = create_engine(f'sqlite:///{settings.SQLITE_DB_NAME}')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def create_db(db_session):
    Base.metadata.create_all(bind=engine)

