#!/usr/bin/python3
from flask import *

app = Flask(__name__)

@app.route('/', methods=["POST"])
def root():
    data = request.get_json()
    print (data)
    return (data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=9999)
