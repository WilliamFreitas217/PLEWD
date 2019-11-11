from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    usuario_email = db.Column(db.String(100), primary_key = True)
    usuario_senha = db.Column(db.String(200), nullable = False)
    usuario_nome = db.Column(db.String(25))
    usuario_telefone = db.Column(db.String(25))

class Produto(db.Model):
    __tablename__ = 'produto'

    produto_id = db.Column(db.String(100), primary_key = True)
    produto_nome = db.Column(db.String(100), nullable = False)
    produto_preco = db.Column(db.Float, nullable = False)
    produto_qtd = db.Column(db.Integer, nullable = False)
    produto_tipo = db.Column(db.Integer, nullable = False)
    usuario_id_fk = db.Column(db.String(100),db.ForeignKey('usuario.usuario_email'))

class Pagamento(db.Model):
    __tablename__ = 'pagamento'

    pag_num_cartao = db.Column(db.String(100), primary_key = True)
    pag_tipo = db.Column(db.Integer, nullable = False)
    pag_vencimento = db.Column(db.String(20), nullable = False)
    pag_cvv = db.Column(db.String(20), nullable = False)
    pag_bandeira = db.Column(db.String(50), nullable = False)
    pag_pais = db.Column(db.String(20), nullable = False)

    usuario_id_fk = db.Column(db.String(100),db.ForeignKey('usuario.usuario_email'))

class Compra(db.Model):
    __tablename__ = 'compra'

    compra_id = db.Column(db.String(100), primary_key = True)
    compra_data = db.Column(db.DateTime, nullable = False)
    compra_total = db.Column(db.Float, nullable = False)
    compra_forma_pag = db.Column(db.Integer, nullable = False)

    usuario_id_fk = db.Column(db.String(100),db.ForeignKey('usuario.usuario_email'))
    produto_id_fk = db.Column(db.String(100),db.ForeignKey('produto.produto_id'))