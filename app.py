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



if __name__=='__main__':
    app.run(port=5000, debug=True)