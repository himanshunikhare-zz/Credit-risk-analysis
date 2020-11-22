from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db =SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('/other-details')
    return render_template('index.html')

@app.route('/other-details', methods=['GET', 'POST'])
def otherdetails():
    if request.method == 'POST':
        return redirect('/result')
    return render_template('form2.html')

@app.route('/result')
def results():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
