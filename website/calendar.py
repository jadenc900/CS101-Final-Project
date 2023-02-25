from flask import Flask, render_template
from arrivaldate_returnlist import *

app = Flask(__name__)

@app.route('/')
def index():
    marked_dates = [arrivalDate, deadline24hr, healthcheck]  # list of dates to be marked
    return render_template('calendar.html', marked_dates=marked_dates)

if __name__ == '__main__':
    app.run(debug=True)