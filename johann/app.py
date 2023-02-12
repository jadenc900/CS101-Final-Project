from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    user = # define the user 
    notifications = # notifications from a Database
    return render_template('inbox.html', notifications=notifications)

if __name__ == "__main__":
    app.run(debug=True, port=5000)