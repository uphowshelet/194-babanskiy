from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
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

if __name__ == "__main__":
    # Инициализация базы данных
    engine = setup_database("sqlite:///database.sqlite")
    session = create_session(engine)

    # Добавить нового клиента в таблицу NationalNames
    new_baby = NationalNames(Id=101, Name="Vanya", Year=2023, Gender="Male", Count=100)
    print(f"Добавлен клиент с идентификатором: {new_baby.Id}")
    session.add(new_baby)
    session.commit()