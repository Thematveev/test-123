from flask import Flask
from constants import INFO

app = Flask(__name__)


@app.route('/')
def main():
    return "Hello world!"


@app.route('/info')
def info_page():
    return f"Your info -> {INFO}"


@app.route('/calc/<a>/<b>')
def calc(a, b):
    return str(int(a) + int(b))


app.run()
