from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
from utilidades import *

class Usuario(db.Model): #Criando classe Python herdando as informações do SQLAlchemy
    __tablename__ = "teste" #Indicando o nome da tabela que será utilizada
    cpf = db.Column(db.String(14), primary_key=True, nullable=False)  #Definindo CPF como chave primária e não permitindo valor nulo
    nome = db.Column(db.String(100), nullable=False)  #Não permitindo valor nulo