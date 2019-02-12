from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2e681a92dab66ec54a2f' 

posts = [
{
    'author':'Chinua Achebe',
    'title': 'Blog Post 1',
    'content':'First post content',
    'date_posted': 'April 20 2018'
},
{
    'author':'Jane Doe',
    'title': 'Blog Post 2',
    'content':'Second post content',
    'date_posted': 'April 24 2018'
}

]

