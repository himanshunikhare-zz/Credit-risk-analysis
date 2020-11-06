from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db =SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')