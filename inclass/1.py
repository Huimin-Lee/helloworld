# from flask import Flask, request
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def contact_list(names=[]):
    name_list = ['yuyu','mimi']
    return render_template('index.html',names=name_list)





# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/')
# @app.route('//<name>')
# def hello(name=None):
#     return render_template('index.html', name=name)

# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)
