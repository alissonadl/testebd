#from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
#Não é necessário obrigatoriamente pois importando * de utilidades já importa isso também.
from utilidades import *

class Teste(db.Model): #Criando classe Python herdando as informações do SQLAlchemy
    __tablename__ = "teste" #Indicando o nome da tabela que será utilizada
    cpf = db.Column(db.String(11), primary_key=True, nullable=False)  #Definindo CPF como chave primária e não permitindo valor nulo
    nome = db.Column(db.String(30), nullable=False)  #Não permitindo valor nulo