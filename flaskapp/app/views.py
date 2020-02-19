from app import app
from flask import request, jsonify

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'The server is online!'