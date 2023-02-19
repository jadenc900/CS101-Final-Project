# everything here runs automatically 

from flask import *

def create_app():
	app = Flask(__name__) # initialize Flask
	app.config['Secret_key'] = "this is a sentence to encrypt the website info"
	
	from .views import views 

	from .authentification import auth

	app.register_blueprint(views, url_prefix = '/')
	app.register_blueprint(auth, url_prefix = '/')

	return app