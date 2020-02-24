import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'yousseframzy'


api = Api(app)

@app.before_first_request
def create_table():
    app_db.create_all()


if __name__=='__main__':
    from db import app_db
    app_db.init_app(app)
    app.run(port=5000, debug=True)