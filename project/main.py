from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db

from project import forms
from flask_sqlalchemy import SQLAlchemy


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = forms.UserForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        formData = {}
        for i in request.form:
            formData[i] = request.form[i]
        print(formData)
        pass

    if form.validate():
        # Save the comment here.
        return redirect(url_for('result.html'))
    else:
        flash('All the form fields are required. ')
    #if request.method == 'POST':
        #return redirect('/other-details')
    return render_template('profile.html',values=forms.data,form=form, name=current_user.name)

@main.route('/result')
@login_required
def result():
    render_template('result.html')