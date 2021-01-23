#for run this project with flask you must named this file((app.py))
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"
    #for run this file write on CMD:flask run
