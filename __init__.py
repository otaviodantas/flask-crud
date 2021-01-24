from flask import Flask, render_template, request, redirect, url_for, flash
from model import db, Company

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud_connect.sqlite3'
db.init_app(app)

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
    company = Company.query.get(id)
    db.session.delete(company)
    db.session.commit()
    return redirect(url_for('init'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        company = Company.query.get(id)
        company.name = request.form['name']
        company.address = request.form['address']
        company.phone = request.form['phone']
        db.session.commit()
        return redirect(url_for('init'))
    else:
        return render_template('edit.html')


if __name__ == '__main__':
    app.run(debug=True)
