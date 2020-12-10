from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db

from project import forms
from flask_sqlalchemy import SQLAlchemy
from final_model import labelencoder_dict, onehotencoder_dict,data
import pandas as pd
import pandas as np

main = Blueprint('main', __name__)
def process(formData):
    test = pd.DataFrame.from_dict(formData)
    for i in labelencoder_dict.keys():
            lea = labelencoder_dict[i]
            lea.fit(test[i])
            print('----')
            test[i] = lea.transform(test[i])

    print("Label Encoder ",test.shape)

    for k in onehotencoder_dict.keys():



            print(k)
            ohe = onehotencoder_dict[k]
            # print(np.array(list(data[i].unique())).reshape(-1,1))
            z = ohe.transform(np.array(list(test[k])).reshape(-1,1)).toarray()
            dfHot = pd.DataFrame(z, columns = [k + str(int(i)) for i in range(z.shape[1])])
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
    process(formData)
    return redirect(url_for('main.result'))

@main.route('/result')
@login_required
def result():
    return render_template('result.html')