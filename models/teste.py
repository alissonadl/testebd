from flask_sqlalchemy import SQLAlchemy
from utilidades import *

class Usuario(db.Model):
    __tablename__ = "teste"
    cpf = db.Column(db.String(14), primary_key=True, nullable=False)  # CPF como chave primária
    nome = db.Column(db.String(100), nullable=False)  # Nome não nulo