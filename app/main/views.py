import render_template() from flask
from . import app

@main.route('/')
def index():

    '''
    View root page function that returns index page and its data
    '''

    return render_template('index.html')