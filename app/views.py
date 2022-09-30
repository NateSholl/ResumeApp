from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/work_history')
def template():
    return render_template('work_history.html')
