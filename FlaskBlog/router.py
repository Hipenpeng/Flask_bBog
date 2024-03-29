from flask import render_template, url_for,flash,redirect
from FlaskBlog import app,db,bcrypt
from FlaskBlog.forms import RegisterForm, LoginForm
from FlaskBlog.models import User
from flask_login import login_user,current_user,logout_user
posts = [
    {
        'author': 'peng',
        'title': 'First',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'peng',
        'title': 'Second',
        'content': 'Second post content',
        'date_posted': 'April 20, 2019'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        val = User.query.filter_by(email=form.email.data).first()
        val1 = User.query.filter_by(email=form.email.data).first()
        if val ==None and val ==None :
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}','success')
            return redirect(url_for('home'))
        else:
            flash(f'The Username and Email should be unique', 'danger')
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
           login_user(user,remember=form.remember.data)
           return redirect(url_for('home'))
        else:
            flash("Login unsuccessfully. Please check username and password",'danger')
    return render_template('login.html',title='Login',form=form)