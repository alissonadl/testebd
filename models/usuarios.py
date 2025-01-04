from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
from utilidades import *

class Usuario(db.Model, UserMixin): #Criando classe Python herdando as informações do SQLAlchemy e UserMixin
    __tablename__ = "usuarios" #Indicando o nome da tabela que será utilizada
    cpf = db.Column(db.String(11), primary_key=True, nullable=False)  #Definindo CPF como chave primária e não permitindo valor nulo
    nome = db.Column(db.String(30), nullable=False)  #Não permitindo valor nulo
    senha = db.Column(db.String(30), nullable=False) #Não permitindo valor nulo

    def __init__ (self, cpf,nome,senha):
        self.cpf = cpf
        self.nome = nome
        self.senha = senha

    def get_id(self):
        return self.cpf