from application import app
from flask import Flask, render_template, request, url_for
from application.model.entity.entregador import Entregador
from application.model.dao.entregador_dao import EntregadorDAO
from application.model.entity.empresa import Empresa
from application.model.dao.empresa_dao import EmpresaDAO

entregador_list = EntregadorDAO(
    [Entregador("12345678900",
               "Carlos Eduardo Ferreira",
               imagem,
               "Utiliza bicicleta",
               "Rio de Janeiro",
               "12345678",
               "RJ",
               "Sou eu, Carlos",
               50.00,
               6
    ),
    Entregador("00000000000",
               "José Ferreira Eduardo",
               imagem,
               "Utiliza moto",
               "Nova Iguaçu",
               "12345000",
               "RJ",
               "Sou eu, José",
               70.00,
               3
    )])


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
    return render_template("home.html", nome=nomeLogin)


@app.route("/login")
def login_gmail():
    nomeLogin = "Login Gmail"
    return render_template("home.html", nome=nomeLogin)
