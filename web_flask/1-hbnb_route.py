#!/usr/bin/python3
"""
 this will starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def redirect():
    return('HBNB')


while __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
