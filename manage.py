# This is controller
from flask import Flask, render_template, request
from model import user


app = Flask(__name__)


@app.route('/')
def default():
    return render_template('landing_page.html')


@app.route('/index')
def go_to_index():
    return render_template('index.html')


@app.route('/index', methods=['POST'])
def login_to_index():
    username = request.form['username']
    password = request.form['password']
    customer = user.User()
    result = customer.sign_in(username, password)
    token = result[0]
    msg = result[1]
    if token[0]:
        print(msg)
        return render_template('index.html')
    else:
        print(msg)
        return render_template('login.html')


@app.route('/login')
def go_to_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def register_to_login():
    username = request.form['username']
    password = request.form['password']
    customer = user.User()
    result = customer.sign_up(username, password)
    token = result[0]
    msg = result[1]
    if token:
        print(msg)
        return render_template('login.html')
    else:
        print(msg)
        return render_template('register.html')


@app.route('/register')
def go_to_register():
    return render_template('register.html')


@app.route('/upload')
def go_to_upload():
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
