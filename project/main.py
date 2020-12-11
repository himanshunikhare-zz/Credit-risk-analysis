from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db

from project import forms
from flask_sqlalchemy import SQLAlchemy
from final_model import labelencoder_dict, onehotencoder_dict,data
import pandas as pd
import numpy as np
import pickle

main = Blueprint('main', __name__)
def process(formData):
    print("DATA RECIEVED")
    test = pd.DataFrame([formData])
    print(test)
    for i in labelencoder_dict.keys():
            lea = labelencoder_dict[i]
            
            print("-------- "+i+"------------")
            i=i.strip()
            print('lea is',lea)
            print(test[i])
            lea.fit(test[i])
            print('----------------------------')
            test[i] = lea.transform(test[i])
    print("FINISHED LABEL ENCODER")
    print("Label Encoder ",test.shape)

    for k in onehotencoder_dict.keys():

            print('-----------'+k+'-------------')
            ohe = onehotencoder_dict[k]
            # print(np.array(list(data[i].unique())).reshape(-1,1))
            print("array", test[k],ohe)
            z = ohe.transform(np.array(list(test[k])).reshape(-1,1)).toarray()
            dfHot = pd.DataFrame(z, columns = [k + str(int(i)) for i in range(z.shape[1])])
            print('***test')
            # if 'level_0' in test.columns:
            #   test.drop('level_0',axis = 1)
            test = test.reset_index(drop = True)
            test = pd.concat([test, dfHot], axis=1)
            test = test.drop(k,axis = 1)
            # test3 = pd.concat([test3,dfHot], axis=1)
            # test3 = test3.reset_index()

    print(test)

    model = pickle.load(open('model.pkl','rb'))
    print(model.predict(test)) 
    return model.predict(test)

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
    print("__++_+_____+++____+_+_+_++++__")
    print("POST")
    form = forms.UserForm(request.form)
    print(form.errors)
    formData = {}
    for i in request.form:
        formData[i] = request.form[i]
    print(formData)
    res = process(formData)
    return render_template('result.html',name=res)

@main.route('/result')
@login_required
def result():
    return render_template('result.html')