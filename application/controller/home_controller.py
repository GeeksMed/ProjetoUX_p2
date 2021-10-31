from application import app
from flask import Flask, render_template, request, url_for
from application.model.entity.entregador import Entregador
from application.model.dao.entregador_dao import EntregadorDAO
from application.model.entity.empresa import Empresa
from application.model.dao.empresa_dao import EmpresaDAO

entregador_list = EntregadorDAO(
    [Entregador("12345678900",
               "Carlos Eduardo Ferreira",
               "img/carlos.png",
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
               "img/jose.png",
               "Utiliza moto",
               "Nova Iguaçu",
               "12345000",
               "RJ",
               "Sou eu, José",
               70.00,
               3
    )])

empresa_list = EmpresaDAO(
    [Empresa("00000000000000",
               "City LTDA",
               "img/city.png",
               "Utiliza bicicleta",
               "Rio de Janeiro",
               "12345678",
               "RJ",
               "Sou eu, City, melhor empresa para limpeza de cidades.",
               50.00,
               6
    ),
    Empresa("12345678901234",
               "Company Eirelli",
               "img/company.png",
               "Utiliza moto",
               "Nova Iguaçu",
               "12345000",
               "RJ",
               "Sou eu, Company, empresa focada em delivery.",
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


@app.route("/list_entregadores", methods=['GET'])
def list_entregadores():
    return render_template("anuncios.html", anuncio_lista=entregador_list.retornar_entregadores())


@app.route("/list_empresas", methods=['GET'])
def list_empresas():
    return render_template("anuncios.html", anuncio_lista=empresa_list.retornar_empresas())


@app.route("/anuncio/<id>", methods=['GET'])
def anuncio_proprio(id):
    for i in entregador_list.retornar_entregadores():
        if i.cpf_cnpj == id:
            return render_template("anuncio.html", anuncio=i)
    for i in empresa_list.retornar_empresas():
        if i.cpf_cnpj == id:
            return render_template("anuncio.html", anuncio=i)

@app.route("/busca")
def busca():
    anuncios_filtrados = []
    palavra_chave = request.args.get('busca')
    for anuncio in entregador_list.retornar_entregadores():
        if palavra_chave in anuncio.nome or palavra_chave in anuncio.descr_breve or palavra_chave in anuncio.descr_completa:
            anuncios_filtrados.append(anuncio)
    for anuncio in empresa_list.retornar_empresas():
        if palavra_chave in anuncio.nome or palavra_chave in anuncio.descr_breve or palavra_chave in anuncio.descr_completa:
            anuncios_filtrados.append(anuncio)
    if len(anuncios_filtrados) > 0:
        for anuncio in anuncios_filtrados:
            print(anuncio.nome)
        return render_template("anuncios.html", anuncio_lista=anuncios_filtrados)
    return render_template("home.html")