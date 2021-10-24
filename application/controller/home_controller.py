from application import app
from flask import Flask, render_template, request, url_for


@app.route('/')
def index():
    return render_template("login.html")


@app.route("/lostpassword") #, methods=["POST"])
def esqueceu():
    return render_template("forget_password.html")


@app.route("/recuperalogin", methods=["POST"])
def recuperar():
    nomeLogin = request.form.get('textarea')
    if nomeLogin == None:
        nomeLogin = "Login Recuperado"
    return render_template("recupera.html", nome=nomeLogin)


@app.route("/newaccount") #, methods=["POST"])
def nova_conta():
    return render_template("novaconta.html")


@app.route("/login", methods=['POST'])
def get_nome():
    nomeLogin = request.form.get('textarea')
    print("nomeLogin = ", nomeLogin)
    if nomeLogin == None or nomeLogin == "":
        nomeLogin = "Welcome Tester"
    return render_template("index.html", nome=nomeLogin)


@app.route("/login")
def login_gmail():
    nomeLogin = "Login Gmail"
    return render_template("index.html", nome=nomeLogin)
