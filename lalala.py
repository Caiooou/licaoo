from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('indexx.html')

@app.route("/cad/usuario")
def usuario():
    return render_template('usuario.html', titulo="Cadastro de Usuario")

@app.route("/cad/caduser", methods=['POST'])
def caduser():
    return request.form    

@app.route("/cad/anuncio")
def anuncio():
    return render_template('anuncio.html', titulo="Fazer Anuncio")

@app.route("/cad/cadprod", methods=['POST'])
def cadprod():
    return "" 

@app.route("/anuncios/pergunta")
def pergunta():
    return render_template('pergunta.html', titulo="Fazer Pergunta no Anuncio")

@app.route("/anuncios/pgt", methods=['POST'])
def pgt():
    print("Pergunta Enviada")
    return ""   

@app.route("/anuncios/compra")
def compra():
    return render_template('compra.html', titulo="Compra do Produto")

@app.route("/anuncios/prodcomp", methods=['POST'])
def prodcomp():
    return ""

@app.route("/anuncios/favoritos")
def favoritos():
    return render_template('favoritos.html', titulo="Anuncios Favoritos")

@app.route("/anuncios/anufav", methods=['POST'])
def anufav():
    return request.form 

@app.route("/config/categoria")
def categoria():
    return render_template('categoria.html')

@app.route("/relatorios/vendas")
def relVendas():
    return cadprod

@app.route("/relatorios/compras")
def relCompras():
    return prodcomp