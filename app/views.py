from flask import render_template
from app import app

@app.route('/')
def home():
    return "<b>Testing, 1, 2, 3.</b>"

@app.route('/template')
def template():
    return render_template('home.html')
