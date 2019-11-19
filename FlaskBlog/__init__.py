from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='1112015112151f5rgg15dsf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.sqlite'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from FlaskBlog import router