from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db/postgres'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
DbSession = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = DbSession()

    try:
        yield db

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()
