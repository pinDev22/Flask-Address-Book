from app import app
#python func to render templates from html
from flask import render_template, flash, redirect, url_for
from app.forms import SignupForm
from app.models import User
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

        # No records match this username or email
        check_user = User.query.filter( (User.username == username) | (User.email == email) ).all()

        if check_user:
            # alert that user record already exists
            flash('A user with that email and/or username already exists.', 'danger')
            return redirect(url_for('signup'))

        new_user = User(email=email, username=username, password=password)
        flash(f"Thank you {first_name} {last_name} for signing up", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)
