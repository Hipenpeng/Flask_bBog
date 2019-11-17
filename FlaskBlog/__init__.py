from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='1112015112151f5rgg15dsf'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from FlaskBlog import router