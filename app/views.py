from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/work_history')
def work_history():
    return render_template('work_history.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/experiments')
def experiments():
    return render_template('experiments.html')