from flask import render_template, request, redirect, url_for, flash
from model import db, Company
from __init__ import app
from helpers import is_null

@app.before_first_request
def create_table():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def init():
    query = Company.query.all()
    return render_template('list.html', company=query, size_data=len(query))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        company = Company(request.form['name'], request.form['address'],
                          request.form['phone'])
        db.session.add(company)
        db.session.commit()

        return redirect(url_for('init'))
    else:
        return render_template('add.html')


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    db.session.delete(Company.query.get(id))
    db.session.commit()
    return redirect(url_for('init'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        company = Company.query.get(id)
        company.name, company.address, company.phone = is_null(company)
        db.session.commit()
        return redirect(url_for('init'))
    else:
        return render_template('edit.html')
