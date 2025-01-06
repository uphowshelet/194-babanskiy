from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import setup_database, create_session, NationalNames, StateNames
from crud import (
    add_national_name, add_state_name, delete_national_name, delete_state_name,
    search_national_names_by_name, search_state_names_by_name
)
app = Flask(__name__)
app.secret_key = 'qwe'
engine = setup_database("sqlite:///database.sqlite")
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    national_names = session.query(NationalNames).limit(50).all()
    state_names = session.query(StateNames).limit(50).all()
    return render_template('index.html', national_names=national_names, state_names=state_names)
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    search_type = request.args.get('type', 'national')
    if search_type == 'national':
        results = search_national_names_by_name(query)
        return render_template('index.html', national_names=results, state_names=[])
    elif search_type == 'state':
        results = search_state_names_by_name(query)
        return render_template('index.html', national_names=[], state_names=results)
    else:
        flash('Неверный тип поиска', 'error')
        return redirect(url_for('index'))
@app.route('/delete/<string:table>/<int:id>', methods=['POST'])
def delete(table, id):
    if table == 'national':
        delete_national_name(id)
        flash(f'Запись с ID {id} удалена из NationalNames', 'success')
    elif table == 'state':
        delete_state_name(id)
        flash(f'Запись с ID {id} удалена из StateNames', 'success')
    else:
        flash('Неверная таблица', 'error')
    return redirect(url_for('index'))
@app.route('/add', methods=['POST'])
def add():
    table = request.form.get('table', 'national')
    name = request.form.get('name', '')
    year = request.form.get('year', '')
    gender = request.form.get('gender', '')
    state = request.form.get('state', '')
    count = request.form.get('count', '')
    if not name or not year or not gender or not count:
        flash('Заполните все обязательные поля', 'error')
        return redirect(url_for('index'))
    try:
        year = int(year)
        count = int(count)
        if table == 'national':
            add_national_name(name, year, gender, count)
            flash(f'Имя "{name}" добавлено в NationalNames', 'success')
        elif table == 'state':
            if not state:
                flash('Для StateNames необходимо указать штат', 'error')
                return redirect(url_for('index'))
            add_state_name(name, year, gender, state, count)
            flash(f'Имя "{name}" добавлено в StateNames', 'success')
        else:
            flash('Неверная таблица', 'error')
    except ValueError:
        flash('Год и количество должны быть числами', 'error')
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
