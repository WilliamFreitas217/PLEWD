#!/usr/bin/env python
# -*- coding: utf-8 -*-m─
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from models import *
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:supersecret@localhost:3306/plewd'

db = SQLAlchemy(app)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            response = make_response(jsonify({'message': 'Token is missing!'}), 401)
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response

        try:
            data = jwt.decode(token, 'PLEWD')
            current_user = Usuario.query.filter_by(usuario_email=data['usuario_email']).first()
        except:
            response = make_response(jsonify({'message': 'Token is missing!'}), 401)
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response

        return f(current_user, *args, **kwargs)

    return decorated

#cadastro
@app.route('/usuario', methods=['POST'])
def cadastro_usuario():
    data = request.get_json()
    if db.session.query(Usuario.usuario_email).filter_by(usuario_email = data['email']).first() is not None:
        response = make_response(jsonify({'message': 'eMAIL já cadastrado!'}), 401)
        return response
    
    novo_usuario = Usuario(usuario_senha = data['senha'],
                    usuario_nome = data['nome'],
                    usuario_telefone = data['telefone'],
                    usuario_email = data['email'])
    novo_pagamento = Pagamento(pag_num_cartao = data['num_cartao'], pag_tipo = data['pag_tipo'],
                    pag_vencimento = data['pag_vencimento'], pag_cvv = data['pag_cvv'], pag_bandeira = ['pag_bandeira'],
                    pag_pais = data['pag_pais'])

    try:
        db.session.add(novo_usuario)
        db.session.add(novo_pagamento)
        db.session.commit()
    except:
        raise 
    response =  make_response(jsonify({'message': 'Usuário Cadastrado!', 'id':novo_usuario.usuario_email}))
    return response

@app.route('/usuario', methods=['GET'])
def perfil():
    try:
        usuarios = Usuario.query.all()
        #pagamento = Pagamento.query.filter_by(usuario_id_fk = usuarios.aluno_email).first()
    except:
        db.session.rollback()
        raise
    
    output = []
    for usuario in usuarios:
        user = {
          
            "senha": usuario.usuario_senha,
            "nome":  usuario.usuario_nome,
            "telefone": usuario.usuario_telefone,
            "email": usuario.usuario_email,
            #"num_cartao": usuarios.usuario_cartao,
            #"pag_tipo":  pagamento.pag_tipo,
            #"pag_vencimento": pagamento.pag_vencimento,
            #"pag_cvv": pagamento.pag_cvv,
            #"pag_bandeira":  pagamento.pag_bandeira,
            #"pag_pais": pagamento.pag_pais
    
        }
        output.append(user)

    return jsonify(output)


@app.route('/login')
def login():
    auth = request.authorization
    erro = None

    if (not auth) or (not auth.username) or (not auth.password):
        erro = 'Login required'

    usuario = Usuario.query.filter_by(usuario_email = auth.username).first()
    if not usuario:
        erro = 'Email não cadastrado'
    
    elif not (usuario.usuario_senha == auth.password):
        erro = 'Senha incorreta'

    if erro is None:
        token = jwt.encode({'usuario_email': usuario.usuario_email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'PLEWD')
        response = make_response(jsonify({'token': token.decode('UTF-8'), 'canLogin':True}))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    
    response = make_response(jsonify({'erro':erro}), 401)
    response.headers['WWW-Authenticate'] = 'Basic realm={}'.format(erro)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
            
@app.route('/produto', methods=['POST'])
@token_required
def cadastrar_produto(current_user):
    data = request.get_json()
    print()
    usuario = Usuario.query.filter_by(usuario_email = current_user.usuario_email).first()

    novo_produto = Produto(
        produto_id = data['nome'] + usuario.usuario_email, produto_nome = data['nome'],
        produto_preco = data['preco'], produto_qtd = data['qtd'], produto_tipo = data['tipo'],
        usuario_id_fk = usuario.usuario_email
    )
    print(novo_produto)
    try:
        db.session.add(novo_produto)
        db.session.commit()
    except:
        raise 
    response = make_response(jsonify({'message': 'Produto Cadastrado!', 'id':novo_produto.produto_nome}))
    return response

@app.route('/usuario/produto', methods = ['GET'])
@token_required
def perfil_privado(current_user):
    produtos = Produto.query.filter_by(usuatrio_id_fk = current_user.usuario_email).first()
    return produtos

@app.route('/produto', methods = ['PUT'])
@token_required
def editar_produto(current_user):
    data = request.get_json()
    produto = Produto.query.filter_by(usuario_id_fk = current_user.usuario_email).first()

    produto_id = data['nome'] + current_user.usuario_email, 
    produto_nome = data['nome'],
    produto_preco = data['preco'], 
    produto_qtd = data['qtd'], 
    produto_tipo = data['tipo'],

    try:
        db.session.add(produto)
        db.session.commit()
    except:
        db.session.rollback()
        raise

    response = make_response(jsonify({'message': 'Produto Alterado!', 'id':novo_produto.produto_nome}))
    return response

@app.route('/pagamento', methods = ['POST'])
@token_required
def add_forma_pagamento(current_user):
    data = request.get_json()
    novo_pagamento = Pagamento(pag_num_cartao = data['num_cartao'], pag_tipo = data['pag_tipo'],
                    pag_vencimento = data['pag_vencimento'], pag_cvv = data['pag_cvv'], 
                    pag_bandeira = ['pag_bandeira'],
                    pag_pais = data['pag_pais'], usuario_id_fk = current_user.usuario_email)
    try:
        db.session.add(novo_pagamento)
        db.session.commit()
    except:
        db.session.rollback()
        raise 
    response =  make_response(jsonify({'message': 'Forma de Pagamento Cadastrada!', 'id':novo_pagamento.usuario_id_fk}))
    return response
    
@app.route('/vendedores', methods=['GET'])
def all_vendedores():
    produtos = Produto.query.all()
    vendedores = []

    for produto in produtos:
        a = Usuario.query.filter_by(usuario_email = produto.usuario_id_fk).first()
        output = {
            "Vendedor:" : a.usuario_nome,
            "Telefone:" : a.usuario_telefone,
            "Email:" : a.usuario_email,
            "Produto": produto.produto_nome
        }
        vendedores.append(output)
    return jsonify(vendedores)
    
@app.route('/produtos', methods=['GET'])
def all_produtos():
    produtos = Produto.query.all()
    p = []

    for produto in produtos:
        a = Usuario.query.filter_by(usuario_email = produto.usuario_id_fk).first()
        if produto.produto_tipo == 1:
            tipo = 'Doce'
        elif produto.produto_tipo == 2:
            tipo = 'salgado'
        else:
            tipo = 'Outros'
        output = {
            "Vendedor:" : a.usuario_nome,
            "Telefone:" : a.usuario_telefone,
            "Email:" : a.usuario_email,
            "Produto": produto.produto_nome,
            "Tipo:" : tipo,
            "Preço" : produto.produto_preco
        }
        p.append(output)

    return jsonify(p)


@app.route('/selecionar/produto/<string:produto_id>')
def selecionar_produto(produto_id):
   
    p = Produto.query.filter_by(produto_id=produto_id).first()
    v = Usuario.query.filter_by(usuario_email = p.usuario_id_fk).first()
    
    if p.produto_tipo == 1:
        tipo = 'Doce'
    elif p.produto_tipo == 2:
        tipo = 'salgado'
    else:
        tipo = 'Outros'
    output = {
        "Vendedor:" : v.usuario_nome,
        "Telefone:" : v.usuario_telefone,
        "Email:" : v.usuario_email,
        "Produto": p.produto_nome,
        "Tipo:" : tipo,
        "Preço" : p.produto_preco,
        "Quantidade" : p.produto_qtd
    }
    return jsonify(output)


@app.route('/', methods=['GET'])
def index():
    return "Hello PLEWD"





if __name__ == '__main__':
    app.run()