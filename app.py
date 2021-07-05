from flask import Flask
from flask import render_template

app = Flask(__name__) # creating an app instance
@app.route("/")
def index():
    return "Welcome to Eng 89 DevOps team "

@app.route("/welcome/")
def welcome():
    return "<h1> This is a heading h1 </h1>"

# create a decorator to route traffic to main page
# display two messages in form of h1 and h2
@app.route("/login/")
def login():
    return "<h1> Welcome to the login page</h1> \n" \"<h3> Please enter your login details below: </h2>"


# return render_template('error.html'), 404
@app.errorhandler(404)
def not_found(error):
    return "<h1> Server error </h1> \n" \
           "<h3> The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application. </h3>"
