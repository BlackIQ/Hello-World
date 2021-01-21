#install flask first.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"
    #for run this file write on CMD:flask run
