from flask import Flask, render_template, request, redirect, url_for, flash
from lab1 import setup_database, create_session, NationalNames, StateNames
from lab1_defs import (
    add_national_name, add_state_name, get_first_50_national_names, get_first_50_state_names,
    delete_national_name, delete_state_name, search_national_names_by_name, search_state_names_by_name
)

app = Flask(__name__)
app.secret_key = 'your_secret_key'
engine = setup_database("sqlite:///database.sqlite")
session = create_session(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/national_names', methods=['GET', 'POST'])
def national_names():
    if request.method == 'POST':
        name = request.form['name']
        year = int(request.form['year'])
        gender = request.form['gender']
        count = int(request.form['count'])
        add_national_name(name, year, gender, count)
        flash("Запись добавлена в NationalNames!")
        return redirect(url_for('national_names'))

    names = get_first_50_national_names()
    return render_template('national_names.html', names=names)

@app.route('/state_names', methods=['GET', 'POST'])
def state_names():
    if request.method == 'POST':
        name = request.form['name']
        year = int(request.form['year'])
        gender = request.form['gender']
        state = request.form['state']
        count = int(request.form['count'])
        add_state_name(name, year, gender, state, count)
        flash("Запись добавлена в StateNames!")
        return redirect(url_for('state_names'))

    names = get_first_50_state_names()
    return render_template('state_names.html', names=names)

@app.route('/delete_national_name/<int:id>')
def delete_national_name_route(id):
    delete_national_name(id)
    flash("Запись удалена из NationalNames!")
    return redirect(url_for('national_names'))

@app.route('/delete_state_name/<int:id>')
def delete_state_name_route(id):
    delete_state_name(id)
    flash("Запись удалена из StateNames!")
    return redirect(url_for('state_names'))

@app.route('/search_national_names', methods=['POST'])
def search_national_names():
    name = request.form['name']
    results = search_national_names_by_name(name)
    return render_template('national_names.html', names=results)

@app.route('/search_state_names', methods=['POST'])
def search_state_names():
    name = request.form['name']
    results = search_state_names_by_name(name)
    return render_template('state_names.html', names=results)

if __name__ == '__main__':
    app.run(debug=True)