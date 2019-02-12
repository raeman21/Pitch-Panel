from flask import Flask, render_template, url_for, flash, redirect
# from . import app
from .forms import RegistrationForm, LoginForm



# app = Flask(__name__)

# app.config['SECRET_KEY'] = '2e681a92dab66ec54a2f' 




@main.route('/home')
def home():
    return  render_template("index.html", posts=posts) 

@main.route('/about')
def about():
    return  render_template("about.html", title='About')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return  render_template("register.html", title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return  render_template("login.html", title='Login', form=form)


