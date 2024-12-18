from flask import Flask, render_template, request #até aqui, já tinhamos visto tudo
import os #Biblioteca para ler arquivos como se fosse um "Sistema Operacional".
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from models.teste import *
from utilidades import *



app = Flask(__name__) #Criando o app flask

load_dotenv()

dbusuario = os.getenv("DB_USERNAME") #Importando informação de usuário do arquivo env
dbsenha = os.getenv("DB_PASSWORD") #Importando informação de senha do arquivo env
host = os.getenv("DB_HOST") #Importando informação de host do arquivo env
meubanco = os.getenv("DB_DATABASE") #Importando informação de banco de dados do arquivo env

conexao = f"mysql+pymysql://{dbusuario}:{dbsenha}@{host}/{meubanco}" #Formatando a linha de conexão com o banco
app.config["SQLALCHEMY_DATABASE_URI"] = conexao #Comunicando com o banco de fato

db = SQLAlchemy(app)

#Rotas:


@app.route('/', methods = ["get","post"])
def inicio():
    return render_template('inicio.html')

@app.route('/enviar', methods = ["post"])
def enviar():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    
    novo_usuario = Usuario(nome=nome, cpf=cpf)
    db.session.add(novo_usuario)
    db.session.commit()
    mensagem = "Usuário cadastrado com sucesso!"

    return render_template('enviar.html', nome = nome, cpf = cpf)