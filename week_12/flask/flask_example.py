from flask import Flask, request

"""
To use this:

1. Ensure you have installed flask using pip3 or PyCharm
2. Open a terminal window in the same folder as this file
3. Enter the command:  export FLASK_APP=flask_example.py
4. Enter the command:  flask run
5. Open a browser and navigate to http://127.0.0.1:5000/ aka localhost:5000
5. You're using flask, a micro-framework
6. Use control-C to shut down the server.
7. So easy.  You're a back-end programmer now, Harry!
"""

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {name}!'

