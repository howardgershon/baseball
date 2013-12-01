from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/viz')
def viz():
    return render_template("viz.html")
