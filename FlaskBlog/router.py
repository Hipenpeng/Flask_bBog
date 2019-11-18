from flask import render_template, url_for,flash,redirect
from FlaskBlog import app,db,bcrypt
from FlaskBlog.forms import RegisterForm, LoginForm
from FlaskBlog.models import User
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
        user = User(username = form.username.data,email=form.email.data, password=hashed_password)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data== 'peng@peng.com' and form.password.data=='password':
            flash("You have logged in!",'success')
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessfully. Please check username and password",'danger')
    return render_template('login.html',title='Login',form=form)