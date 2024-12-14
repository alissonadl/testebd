from flask import Flask, render_template, request #até aqui, já tinhamos visto tudo
import os #Biblioteca para ler arquivos como se fosse um "Sistema Operacional".
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

db = SQLAlchemy(app)

dbusuario = os.getenv("DB_USERNAME")
dbsenha = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
meubanco = os.getenv("DB_DATABASE")

conexao = f"mysql+pymysql://{dbusuario}:{dbsenha}@{host}/{meubanco}"
app.config["SQLALCHEMY_DATABASE_URI"] = conexao


@app.route('/', methods = ["get","post"])
def inicio():
    return render_template('inicio.html')

@app.route('/enviar', methods = ["post"])
def enviar():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    return render_template('enviar.html', nome = nome, cpf = cpf)