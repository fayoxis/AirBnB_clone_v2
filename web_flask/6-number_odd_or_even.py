#!/usr/bin/python3
"""
this will starts a Flask web application:
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def redirect():
    return('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    return('C {}'.format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text_py>', strict_slashes=False)
def python(text_py='is cool'):
    return('Python {}'.format(text_py.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_number(n):
    return(render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    return (render_template('6-number_odd_or_even.html', n=n))


while __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
