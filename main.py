"""`main` is the top level module for your Bottle application."""

# import the Bottle framework
from bottle import Bottle, static_file
import json

# Create the Bottle WSGI application.
bottle = Bottle()
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# Define an handler for the root URL of our application.
@bottle.route('/recipes')
def root():
    return static_file('data/small_data.json', root='.')
@bottle.route('/recipe/<id>')
def data(id):
    my_data = open("./data/small_data.json").read()
    jsonDataAsPythonValue = json.loads(my_data)
    return jsonDataAsPythonValue[int(id)]

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.'

@bottle.error(500)
def error_500(error):
    """Return a custom 500 error."""
    return 'Sorry, internal server error.'