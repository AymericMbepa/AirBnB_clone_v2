#!/usr/bin/python3
"""
this module starts a Flask web application that listens on 0.0.0.0, port 5000
It define a single route at the Root URL ('/') that displays 'Hello HBNB!'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """
    this function is the view function for the Root URL ('/')
    It return the string with a message as a response to the request
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
