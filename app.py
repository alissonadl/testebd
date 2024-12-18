from flask import Flask, render_template, request #até aqui, já tinhamos visto tudo
import os #Biblioteca para ler arquivos como se fosse um "Sistema Operacional"
from dotenv import load_dotenv #Biblioteca para trabalhar com arquivos env
from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
from models.usuario import * #Importando o nosso modelo de classe que será uma tabela no banco de dados
from utilidades import * #Importando a instância do banco de dados lá no arquivo utilidades


app = Flask(__name__) #Criando o app Flask

load_dotenv() #Carrega variáveis do nosso arquivo .flaskenv

dbusuario = os.getenv("DB_USERNAME") #Importando informação de usuário do arquivo env
dbsenha = os.getenv("DB_PASSWORD") #Importando informação de senha do arquivo env
host = os.getenv("DB_HOST") #Importando informação de host do arquivo env
meubanco = os.getenv("DB_DATABASE") #Importando informação de banco de dados do arquivo env


conexao = f"mysql+pymysql://{dbusuario}:{dbsenha}@{host}/{meubanco}" #Formatando a linha de conexão com o banco
app.config["SQLALCHEMY_DATABASE_URI"] = conexao #Criando uma "rota" de comunicação
db.init_app(app) #Sinaliza que o banco será gerenciado pelo app


#Rotas:

#Rota inicial
@app.route('/', methods = ["get","post"])
def inicio():
    return render_template("inicio.html")


#Função de cadastrar usuario no banco de dados
#IMPORTANTE: ISSO SERIA O "C" DO C.R.U.D. Ou seja, Create.
@app.route('/create', methods = ["get","post"])
def create():
    return render_template("create.html")


@app.route('/enviar', methods = ["get","post"])
def enviar():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    novo_usuario = Usuario(nome=nome, cpf=cpf) #Criando um objeto da classe usuário que será uma nova informação no banco
    db.session.add(novo_usuario) #Adiciona o objeto novo_usuario à sessão do banco de dados, preparando-o para ser salvo
    db.session.commit() #Confirma e salva a nova informação de fato
    return render_template('enviar.html', nome = nome, cpf = cpf)


#Função para recuprar dados do banco.
#IMPORTANTE: ISSO SERIA O "R" DO C.R.U.D. Ou seja, Recovery
@app.route("/recovery", methods = ["get", "post"])
def recovery():
    return render_template("recovery.html")

@app.route("/mostrar", methods = ["get", "post"])
def mostrar():
    cpf = request.form.get('cpf')
    recovery_usuario = Usuario.query.get(cpf) #Precisa informar a primary key da tupla. Isso recebe os dados da tupla para essa variável.
    return render_template("mostrar.html", usuario = recovery_usuario) #recovery_usuario recebe um objeto da classe Usuario já cadastrado no banco. 


#Função para atualizar informações do banco. {
#IMPORTANTE: ISSO SERIA O "U" DO C.R.U.D. Ou seja, Update
@app.route("/update", methods = ["get", "post"])
def update():
    return render_template("update.html")

@app.route("/atualizado", methods=["get", "post"])
def atualizar():
    novo_nome = request.form.get("novo_nome")  #Pega o novo nome enviado pelo usuário
    cpf = request.form.get("cpf")
    usuario = Usuario.query.get(cpf)  #Busca um usuário pelo CPF do usuário
    usuario.nome = novo_nome  # Atualiza o nome
    db.session.commit()  # Salva a alteração no banco de dados
    return render_template("atualizado.html", usuario = usuario)


#Função para deletar informações do banco. {
#IMPORTANTE: ISSO SERIA O "D" DO C.R.U.D. Ou seja, Delete
@app.route("/delete", methods = ["get", "post"])
def delete():
    return render_template("delete.html")

@app.route("/deletado", methods = ["get", "post"])
def deletado():
    cpf = request.form.get("cpf")
    usuario = Usuario.query.get(cpf)  #Busca um usuário pelo CPF do usuário
    db.session.delete(usuario)
    db.session.commit()
    return render_template("deletado.html", cpf = cpf)