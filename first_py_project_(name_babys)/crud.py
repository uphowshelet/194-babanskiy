from orm import setup_database, create_session, NationalNames, StateNames

# Инициализация базы данных
engine = setup_database("sqlite:///database.sqlite")
session = create_session(engine)

def generate_unique_id(session, model):
    max_id = session.query(model).order_by(model.Id.desc()).first()
    return max_id.Id + 1 if max_id else 1

#вывод первых 50 пользователей
def get_first_50_national_names():
    babies = session.query(NationalNames).limit(50).all()
    for baby in babies:
        print(f"NationalNames: ID: {baby.Id}, Name: {baby.Name}, Year: {baby.Year}, Gender: {baby.Gender}, Count: {baby.Count}")
    return babies

def get_first_50_state_names():
    babies = session.query(StateNames).limit(50).all()
    for baby in babies:
        print(f"StateNames: ID: {baby.Id}, Name: {baby.Name}, Year: {baby.Year}, Gender: {baby.Gender}, State: {baby.State}, Count: {baby.Count}")
    return babies

# CREATE (Создание)
def add_national_name(name, year, gender, count):
    new_id = generate_unique_id(session, NationalNames)
    new_baby = NationalNames(Id=new_id, Name=name, Year=year, Gender=gender, Count=count)
    session.add(new_baby)
    session.commit()
    print(f"Baby with name '{name}' added with ID: {new_baby.Id}")
    return new_baby.Id

def add_state_name(name, year, gender, state, count):
    new_id = generate_unique_id(session, StateNames)
    new_baby = StateNames(Id=new_id, Name=name, Year=year, Gender=gender, State=state, Count=count)
    session.add(new_baby)
    session.commit()
    print(f"Baby with name '{name}' added with ID: {new_baby.Id}")
    return new_baby.Id

# READ (Чтение)
def get_national_name_by_id(id):
    baby = session.query(NationalNames).filter_by(Id=id).first()
    if baby:
        print(f"NationalNames: ID: {baby.Id}, Name: {baby.Name}, Year: {baby.Year}, Gender: {baby.Gender}, Count: {baby.Count}")
        return baby
    else:
        print(f"NationalNames with ID {id} not found.")
        return None

def get_state_name_by_id(id):
    baby = session.query(StateNames).filter_by(Id=id).first()
    if baby:
        print(f"StateNames: ID: {baby.Id}, Name: {baby.Name}, Year: {baby.Year}, Gender: {baby.Gender}, State: {baby.State}, Count: {baby.Count}")
        return baby
    else:
        print(f"StateNames with ID {id} not found.")
        return None

# UPDATE (Обновление)
def update_national_name(id, name=None, year=None, gender=None, count=None):
    baby = session.query(NationalNames).filter_by(Id=id).first()
    if baby:
        if name: baby.Name = name
        if year: baby.Year = year
        if gender: baby.Gender = gender
        if count: baby.Count = count
        session.commit()
        print(f"NationalNames ID {id} updated.")
        return baby
    else:
        print(f"NationalNames with ID {id} not found.")
        return None

def update_state_name(id, name=None, year=None, gender=None, state=None, count=None):
    baby = session.query(StateNames).filter_by(Id=id).first()
    if baby:
        if name: baby.Name = name
        if year: baby.Year = year
        if gender: baby.Gender = gender
        if state: baby.State = state
        if count: baby.Count = count
        session.commit()
        print(f"StateNames ID {id} updated.")
        return baby
    else:
        print(f"StateNames with ID {id} not found.")
        return None

# DELETE (Удаление)
def delete_national_name(id):
    baby = session.query(NationalNames).filter_by(Id=id).first()
    if baby:
        session.delete(baby)
        session.commit()
        print(f"NationalNames ID {id} deleted.")
    else:
        print(f"NationalNames with ID {id} not found.")

def delete_state_name(id):
    baby = session.query(StateNames).filter_by(Id=id).first()
    if baby:
        session.delete(baby)
        session.commit()
        print(f"StateNames ID {id} deleted.")
    else:
        print(f"StateNames with ID {id} not found.")

def search_national_names_by_name(name):
    babik = session.query(NationalNames).filter(NationalNames.Name.ilike(f"{name}")).all()
    if babik:
        for baby in babik:
            print(f"NationalNames: ID: {baby.Id}, Name: {baby.Name}, Year: {baby.Year}, Gender: {baby.Gender}, Count: {baby.Count}")
        return babik
    else:
        print(f"Не найдено записей с именем '{name}'.")
        return None

def search_state_names_by_name(name):
    babik = session.query(StateNames).filter(StateNames.Name.ilike(f"{name}")).all()
    if babik:
        for baby in babik:
            print(f"StateNames: ID: {baby.Id}, Name: {baby.Name}, Year: {baby.Year}, Gender: {baby.Gender}, State: {baby.State}, Count: {baby.Count}")
        return babik
    else:
        print(f"Не найдено записей с именем '{name}'.")
        return None

def analyze(session, model):
    full = session.query(model).count()
    m_count = session.query(model).filter(model.Gender == 'M').count()
    f_count = session.query(model).filter(model.Gender == 'F').count()
    if full > 0:
        m_percentage = (m_count / full) * 100 
    else:
        0
    if full > 0:    
        f_percentage = (f_count / full) * 100 
    else:
        0
    
    return m_percentage, f_percentage



# Примеры использования
if __name__ == "__main__":
    # Создание
    national_id = add_national_name("Vanya", 2017, "M", 100)
    state_id = add_state_name("Vanya", 2017, "M", "Tomsk", 50)

    # Чтение
    get_national_name_by_id(national_id)
    get_state_name_by_id(state_id)

    # Обновление
    update_national_name(national_id, name="Ivan", count=150)
    update_state_name(state_id, name="Ivan", state="Tomsk")

    # Чтение после обновления
    get_national_name_by_id(national_id)
    get_state_name_by_id(state_id)

    # Удаление
    delete_national_name(national_id)
    delete_state_name(state_id)

    # Чтение после удаления
    get_national_name_by_id(national_id)
    get_state_name_by_id(state_id)

    # Чтение первых 50 пользователей
    # get_first_50_national_names()
    # get_first_50_state_names()

    # Закрыть сессию
    session.close()

    get_national_name_by_id(1)
    get_state_name_by_id(1)

    # search_national_names_by_name("Mary")
    # search_state_names_by_name("Ivan")

