from flask import request

def is_null(company: object) -> str:
    name = [company.name if request.form['name'] is '' else request.form['name']]
    address = [company.address if request.form['address'] is '' else request.form['address']]
    phone = [company.phone if request.form['phone'] is '' else request.form['phone']]
    return *name, *address, *phone
