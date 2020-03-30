from flask import Blueprint, render_template

home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def home():
    return '<h1>Hello Flask!</h1>'


@home.route('/index')
def index():
    # do some stuff
    print('index.html is called.')

    return render_template('home/index.html')
