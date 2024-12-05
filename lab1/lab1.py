from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Таблица NationalNames
class NationalNames(Base):
    __tablename__ = 'NationalNames'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Year = Column(Integer)
    Gender = Column(String)
    Count = Column(Integer)

# Таблица StateNames
class StateNames(Base):
    __tablename__ = 'StateNames'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Year = Column(Integer)
    Gender = Column(String)
    State = Column(String)
    Count = Column(Integer)

# Настройка подключения к базе данных
def setup_database(database_path="sqlite:///database.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine

# Создание сессии
def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
