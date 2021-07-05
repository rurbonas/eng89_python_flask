# Model View Controller - MVC - with Python Flask
## Python Flask
- Flask is a python micro-framework
- Flask is used to develop web apps
- Flask must first be installed in the app.py (using pip method), and an instance created
```python
from flask import Flask
app = Flask(__name__)
```
- A function is created for the main/default page using `@app.route` decorator. The "/" represents the main page
```python
@app.route("/") # decorating our function with @app.route to set route in browser
def index():
    return "Welcome to Eng 89 DevOps team "
```
- `Flask run` terminal command is used to run this code file
- Routes to further sub-pages with more functions can be created in the same way
- Defining the routes as `"/welcome/` with both / captures the input if it is just `"/welcome"` as well
```python
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
```
## HTML
## JavaScript
## Bootstrap