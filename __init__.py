from flask import Flask
from model import db
from env import PATH_URI_BD, SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = PATH_URI_BD
app.secret_key = SECRET_KEY

db.init_app(app)

from viwers import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
