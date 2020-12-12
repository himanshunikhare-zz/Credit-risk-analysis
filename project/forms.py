from _datetime import datetime
import pandas as pd
import numpy as np
from wtforms import Form, TextField,RadioField,SelectField,validators
from wtforms.fields.html5 import DecimalRangeField

def createForm(data):
    queryList = []
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
        queryList.append("%s=%s" % (var[1],formElement))
        # exec("%s=%s" % (var[1],formElement))
    return queryList

class UserForm(Form):
    data=pd.read_csv("csv_files/createForm1.csv")
    queries = createForm(data)
    for i in queries:
        exec(i)

class UserForm2(Form):
    data=pd.read_csv("csv_files/createForm2.csv")
    queries = createForm(data)
    for i in queries:
        exec(i)
    
