from flask import Flask, render_template, request, redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime
import pandas as pd
import numpy as np
from wtforms import Form, TextField,RadioField,SelectField,validators
from wtforms.fields.html5 import DecimalRangeField


from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import PasswordField, BooleanField,StringField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db =SQLAlchemy(app)
data=pd.read_csv("./temp.csv")
#print(data.keys())
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#Changes
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('Email ID', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def reg_index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('index'))
            else:
                flash('Please check your login details and try again.')
                return redirect(url_for('login'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()


    user = User.query.filter_by(email=form.email.data).first() 
    # if this returns a user, then the email already exists in database

    # if a user is found, we want to redirect back to signup page so user can try again
    if user: 
        flash('Email address already exists')
        return redirect(url_for('signup'))

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('reg_index'))



class UserForm(Form):
    for i in data:
        # print(data[i])
        var = i.split('/')
        # print(var) 
        print(var[1])
        if data[i][0] == 'textbox':
            formElement='TextField("%s",validators=[validators.required()], default="please add content")' %(var[0])

        elif data[i][0] == 'radio':
            choice = list(data[i][1:].dropna().unique().tolist())
            choiceStr=''
            for k in choice:
                ch = k.split('/')
                if len(ch)>1:
                    choiceStr +="('"+ch[1]+"','"+ch[0]+"')," 
                else:
                    choiceStr +="('"+k+"','"+k+"'),"
            formElement = 'RadioField("%s",validators=[validators.required()],choices=[%s], default="%s")' %(var[0],choiceStr, choice[0])

        elif data[i][0] == 'dropdown':
            choice = list(data[i][1:].dropna().unique().tolist())
            # choice.remove('X')
            choiceStr=''
            for k in choice:
                ch = k.split('/')
                if len(ch)>1:
                    choiceStr +="('"+ch[1]+"','"+ch[0]+"')," 
                else:
                    choiceStr +="('"+k+"','"+k+"')," 
            # print(choiceStr)
            formElement = 'SelectField("%s",validators=[validators.required()],choices=[%s])' %(var[0],choiceStr)

        else:
            choiceStr=''
            choice = list(data[i][1:].dropna().unique().tolist())
            for k in range(int(choice[0]),int(choice[1])+1):
                k = str(k)
                choiceStr +="('"+k+"','"+k+"')," 
            # print(choiceStr)
            formElement = 'SelectField("%s",validators=[validators.required()],choices=[%s])' %(var[0],choiceStr)
            
        exec("%s=%s" % (var[1],formElement))



@app.route('/test', methods=['GET', 'POST'])# route '/' changed to 'test'
def index():
    form = UserForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        formData = {}
        for i in request.form:
            formData[i] = request.form[i]
        print(formData)
        pass

    if form.validate():
        # Save the comment here.
        flash('Succesfully submitted')
        return render_template('result.html')
    else:
        flash('All the form fields are required. ')
    #if request.method == 'POST':
        #return redirect('/other-details')
    return render_template('index2.html',values=data,form=form)# index changed to index2

@app.route('/other-details', methods=['GET', 'POST'])
def otherdetails():
    if request.method == 'POST':
        return redirect('/result')
    return render_template('form2.html')

@app.route('/result')
def results():
    return render_template('result.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
