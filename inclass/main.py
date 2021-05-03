from flask import Flask, abort, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

# #redirect demo
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST' and request.form['username'] == 'admin':
#         return redirect(url_for('success'))
#     return redirect(url_for('index'), 302)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return'logged in successfully'





# from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
# import os
# app = Flask(__name__)

# app.config['UPLOAD_FOLDER'] = os.getcwd()+'/media/'
# app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024 #限制大小16MB

# @app.route('/')
# def upload():
#     return render_template('upload.html')

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
#         return 'flie uploaded successfully'