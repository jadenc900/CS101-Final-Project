# storing the standard routes of the website

from flask import Blueprint

# define the URLs of the app - define each page in its own file, rather than one

views = Blueprint('views', __name__)

@views.route('/')
def homepage(): #runs when accessing url.sthsth'/'
    return "<h1> Test </h1>" # heading, text: "Test"

