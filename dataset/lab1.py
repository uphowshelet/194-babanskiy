from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Таблица ProductId
class NationalNames(Base):
    __tablename__ = 'NationalNames'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Year= Column(Integer)
    Gender= Column(String)
    Count= Column(Integer)

class StateNames(Base):

    def setup_database(database_path="sqlite:///Chinook_Sqlite.sqlite"):
        engine = create_engine(database_path)
        Base.metadata.create_all(engine)
        return engine

    # Создание сессии
    def create_session(engine):
        Session = sessionmaker(bind=engine)
        return Session()

    engine = setup_database("sqlite:///Chinook_Sqlite.sqlite")
    session = create_session(engine)
    # Добавить нового артиста

    session.add(new_artist)
    session.commit()
