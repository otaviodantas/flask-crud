from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud_connect.sqlite3'

db = SQLAlchemy(app)

class Company(db.Model):
    __tablename__ = 'Company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    phone = db.Column(db.Integer())
    address = db.Column(db.String())

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

@app.route('/', methods=['GET', 'POST'])
def init():
    return render_template('list.html', company = Company.query.all())


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        company = Company(request.form['name-add'], request.form['address'],
                          request.form['phone'])
        db.session.add(company)
        db.session.commit()

        return redirect(url_for('init'))
    else:
        return render_template('add.html')


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    company = Company.query.get(id)
    db.session.delete(company)
    db.session.commit()
    return redirect(url_for('init'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        company = Company.query.get(id)
        company.name = request.form['name-edit']
        company.address = request.form['address-edit']
        company.phone = request.form['phone-edit']
        db.session.commit()
        return redirect(url_for('init'))
    else:
        return render_template('edit.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
