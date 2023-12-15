from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get("User-Agent")
    return '''
    <h1>Hello, Flask</h1>
    <p>Your browser is {}</p?
    '''.format(user_agent), 200


@app.route('/user/<name>')
def user(name):
    return '''
    <h1>Hello Flask</h1>
    <p>Hello {}, Welcome back!!
    '''.format(name), 201


@app.route('/error')
def failure():
    return '''<h1>Bad Request</h1>
    <p>This is gonna spew some error message on the website</p>
    ''', 400


@app.route('/makeRequest')
def make_requests():
    response = make_response('<h3>This document carries a cookie</h3>')
    response.set_cookie('answer', 42)
    return response, 200
