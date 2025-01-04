from flask_login import UserMixin
#from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
#Não é necessário obrigatoriamente pois importando * de utilidades já importa isso também.
from utilidades import *

class Usuario(db.Model, UserMixin): #Criando classe Python herdando as informações do SQLAlchemy e UserMixin
    __tablename__ = "usuarios" #Indicando o nome da tabela que será utilizada
    cpf = db.Column(db.String(11), primary_key=True, nullable=False)  #Definindo CPF como chave primária e não permitindo valor nulo
    nome = db.Column(db.String(30), nullable=False)  #Não permitindo valor nulo
    senha = db.Column(db.String(30), nullable=False) #Não permitindo valor nulo

    def get_id(self): #Função para pegar o identificador do usuário (necessário para login)
        return self.cpf