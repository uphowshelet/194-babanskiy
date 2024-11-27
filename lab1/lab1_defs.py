from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lab1 import setup_database, create_session, NationalNames, StateNames

# Инициализация базы данных
engine = setup_database("sqlite:///database.sqlite")
session = create_session(engine)

# CREATE (Создание)
def add_NationalNames(id, name, year, gender, count):
    new_baby = NationalNames(
        Id=id,
        Name=name,
        Year=year,
        Gender=gender,
        Count=count,
    )
    session.add(new_baby)
    session.commit()
    print(f"Baby with name '{name}' added with ID: {new_baby.Id}")
    return new_baby.Id

def add_StateNames(id, name, year,gender, state, count):
    new_baby1 = StateNames(
        Id=id,
        Name=name,
        Year=year,
        Gender=gender,
        State=state,
        Count=count,
    )
    session.add(new_baby1)
    session.commit()
    print(f"Baby with name '{name}'added with ID: {new_baby1.Id}")
    return new_baby1.Id

# READ (Чтение)
def get_NationalNames_by_id(id):
    baby = session.query(NationalNames).filter_by(Id=id).first()
    if baby:
        print(f"NationalNames: ID: {baby.Id}, Name: {baby.Name}, Year: {baby.Year}, Gender: {baby.Gender}, Count: {baby.Count}")
        return baby
    else:
        print(f"NationalNames with ID {id} not found.")
        return None

def get_all_NationalNames():
    babies = session.query(NationalNames).all()
    for baby in babies:
        print(f"NationalNames: ID: {baby.Id}, Name:{baby.Name}, Year:{baby.Year}, Gender: {baby.Gender},Count: {baby.Count}")
    return babies

def get_StateNames_by_id(id):
    baby = session.query(StateNames).filter_by(Id=id).first()
    if baby:
        print(f"StateNames: ID:{baby.Id}, Name:{baby.Name}, Year: {baby.Year}, Gender: {baby.Gender}, State: {baby.State},Count: {baby.Count}")
        return baby
    else:
        print(f"StateNames with ID {id} not found.")
        return None

def get_all_StateNames():
    babies = session.query(StateNames).all()
    for baby in babies:
        print(f"StateNames: ID: {baby.Id}, Name: {baby.Name}, Year:{baby.Year}, Gender:{baby.Gender}, State: {baby.State}, Count:{baby.Count}")
    return babies

# UPDATE (Обновление)
def update_NationalNames(id, name=None, year=None, gender=None, count=None):
    baby = session.query(NationalNames).filter_by(Id=id).first()
    if baby:
        if name:baby.Name = name
        if year:baby.Year = year
        if gender:baby.Gender = gender
        if count:baby.Count = count
        session.commit()
        print(f"NationalNames ID{id} updated.")
        return baby
    else:
        print(f"NationalNames with ID {id}not found.")
        return None

def update_StateNames(id, name=None,year=None, gender=None,state=None, count=None ):
    baby=session.query(StateNames).filter_by(Id=id).first()
    if baby:
        if name:baby.Name =name
        if year:baby.Year = year
        if gender:baby.Gender= gender
        if state:baby.State= state
        if count:baby.Count =count
        session.commit()
        print(f"StateNames ID {id}updated.")
        return baby
    else:
        print(f"StateNames with ID {id} not found.")
        return None

# DELETE (Удаление)
def delete_NationalNames(id):
    baby = session.query(NationalNames).filter_by(Id=id).first()
    if baby:
        session.delete(baby)
        session.commit()
        print(f"NationalNames ID {id} deleted.")
    else:
        print(f"NationalNames with ID {id} not found.")

def delete_StateNames(id):
    baby = session.query(StateNames).filter_by(Id=id).first()
    if baby:
        session.delete(baby)
        session.commit()
        print(f"StateNames ID {id} deleted.")
    else:
        print(f"StateNames with ID {id} not found.")




# Примеры использования
if __name__ == "__main__":
    #cоздание
    national_id = add_NationalNames(1,"Vanya",2017,"male",100)
    state_id = add_StateNames(1,"Vanya",2017,"male","Tomsk",50)
    #чтение
    get_NationalNames_by_id(national_id)
    get_all_NationalNames()
    get_StateNames_by_id(state_id)
    get_all_StateNames()
    #обновление
    update_NationalNames(national_id,name="Ivan",count=150)
    update_StateNames(state_id,name="Ivan",state="Tomsk")
    #удаление
    delete_NationalNames(national_id)
    delete_StateNames(state_id)