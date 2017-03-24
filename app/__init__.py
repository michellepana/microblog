from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap 
from flask.ext.mail import Mail
from flask.ext.moment import Moment 
from flask.ext.sqlalchemy import SQLAlchemy 
from config import Config



from flask.ext.login import LoginManager

bootstrap=Bootstrap()
mail=Mail()
moment=Moment()
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection='Strong'
login_manager.login_view='auth.login'

def create_app(config_name):
	app=Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootsrap.init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	login_manager.init_app(app)
	return app

