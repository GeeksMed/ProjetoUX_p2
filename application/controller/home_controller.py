from application import app
from flask import Flask, render_template, request, url_for

@app.route('/')
def index():
    return render_template("login.html")

@app.route("/login/", methods=['POST'])
def get_nome():
    nomeLogin = request.form.get('textarea')
    return render_template("home.html", nome = nomeLogin)