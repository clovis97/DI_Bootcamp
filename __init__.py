import flask
import flask_sqlalchemy
import flask_migrate
import psycopg2
import os
basedir = os.path.abspath(os.path.dirname(__file__)) # Try to avoid hardcoding paths, use os
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'ecole.db')
app.config['SECRET_KEY'] = 'thisisanykey'
db      = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
from app import routes,error_handlers,models