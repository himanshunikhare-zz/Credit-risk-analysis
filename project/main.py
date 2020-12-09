from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db

from project import forms
from flask_sqlalchemy import SQLAlchemy


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    form = forms.UserForm(request.form)
    print(form.errors)
    return render_template('profile.html',values=forms.data,form=form, name=current_user.name)

@main.route('/profile', methods=["POST"])
@login_required
def profile_post():
    print("POST")
    form = forms.UserForm(request.form)
    print(form.errors)
    formData = {}
    for i in request.form:
        formData[i] = request.form[i]
    print(formData)
    return redirect(url_for('main.result'))

@main.route('/result')
@login_required
def result():
    return render_template('result.html')