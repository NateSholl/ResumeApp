from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/work_history')
def template():
    return render_template('work_history.html')

@app.route('/contact')
def template():
    return render_template('contact.html')

# @app.route('/experiments')
# def template():
#     return render_template('experiments.html')