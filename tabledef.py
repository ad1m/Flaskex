from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from settings import SQLALCHEMY_DATABASE_URI

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(SQLALCHEMY_DATABASE_URI)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(30))
    email = Column(String(50))
    c1 = Column(String(15))
    c2 = Column(String(15))

    def __repr__(self):
        return '<User %r>' % self.username

engine = db_connect()
# Create Models
Base.metadata.create_all(engine)
