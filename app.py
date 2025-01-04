from flask import Flask, render_template, redirect, request #até aqui, já tinhamos visto tudo, menos o redirect
import os #Biblioteca para ler arquivos como se fosse um "Sistema Operacional"
from dotenv import load_dotenv #Biblioteca para trabalhar com arquivos env
from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
from models.teste import * #Importando o nosso modelo de classe que será uma tabela no banco de dados
from models.usuarios import * #Importando o modelo de classe de usuários
from utilidades import * #Importando a instância do banco de dados lá no arquivo utilidades
from flask_login import LoginManager, login_user, logout_user, login_required #importando ferramentas para login

app = Flask(__name__) #Criando o app Flask

load_dotenv() #Carrega variáveis do nosso arquivo .flaskenv

dbusuario = os.getenv("DB_USERNAME") #Importando informação de usuário do arquivo env
dbsenha = os.getenv("DB_PASSWORD") #Importando informação de senha do arquivo env
host = os.getenv("DB_HOST") #Importando informação de host do arquivo env
meubanco = os.getenv("DB_DATABASE") #Importando informação de banco de dados do arquivo env
conexao = f"mysql+pymysql://{dbusuario}:{dbsenha}@{host}/{meubanco}" #Formatando a linha de conexão com o banco
app.config["SQLALCHEMY_DATABASE_URI"] = conexao #Criando uma "rota" de comunicação
db.init_app(app) #Sinaliza que o banco será gerenciado pelo app
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') #Importando a secret key do flaskenv
lm.init_app(app) #Sinalizando que o loginManager será gerenciado pelo app

#Criando a função de carregar informações do usuário do banco de dados

@lm.user_loader #Função reservada do login manager para buscar usuário no banco de dados pela primary key (cpf_usuario no neste caso)
def load_user(cpf_usuario):
    return Usuario.query.get(cpf_usuario) #Busca no banco as informações associadas com esta chave

#Rotas:

#Rota inicial
@app.route('/', methods = ["get", "post"])
def inicio():
    return render_template("inicio.html")

#Rotas de login e cadastro

@app.route('/login', methods = ["get", "post"])
def login():
    return render_template("login.html")

@app.route('/autenticacao', methods = ["get", "post"])
def autenticacao():
    cpf = request.form.get('cpf')
    senha = request.form.get('senha')
    usuario = load_user(cpf)
    if usuario == None: #Se o usuário não for encontrado
        msg = "Usuário não encontrado"
        return render_template("login.html", msg = msg)

    if usuario.cpf == cpf and usuario.senha == senha: # Se der certo
        login_user(usuario) #Efetua o login do usuário "iniciando uma sessão"
        return render_template("autenticacao.html", usuario = usuario)
    
    else: #Se o usuário for encontrado, mas o login falhar (erro de senha)
        msg = "Erro nas credenciais"
        return render_template("login.html", msg = msg)

@app.route('/logout', methods = ["get", "post"]) #Rota para deslogar usuário
@login_required #Sinalizando que o usuário só pode acessar essa página se fez o login
def logout():
    logout_user() #Função do pacote de login manager
    return redirect("login") #redireciona para /login

@app.route('/cadastro', methods = ["get", "post"])
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods = ["get", "post"]) #Tudo aqui vimos no CREATE do banco de dados
def cadastrar():
    cpf = request.form.get("cpf")
    nome = request.form.get("nome")
    senha = request.form.get("senha")
    novo_usuario = Usuario(cpf=cpf, nome=nome, senha=senha)
    db.session.add(novo_usuario)
    db.session.commit()
    return render_template("cadastrar.html", usuario=novo_usuario)

@app.route("/logado", methods = ["get", "post"])
@login_required #Sinalizando que o usuário só pode acessar essa página se fez o login
def logado():
    return render_template("logado.html")

#Personalização de rotas de erro
#Pagina do error 401 (Não autorizado, login não feito)
@app.errorhandler(401)
def erro401(error):
    return render_template('erro401.html'), 401

#Pagina do error 404 (Página não existe)
@app.errorhandler(404)
def erro401(error):
    return render_template('erro404.html'), 404


#Rotas para C.R.U.D:

#Função de cadastrar usuario no banco de dados
#IMPORTANTE: ISSO SERIA O "C" DO C.R.U.D. Ou seja, Create.
@app.route('/create', methods = ["get","post"])
def create():
    return render_template("create.html")


@app.route('/enviar', methods = ["get","post"])
def enviar():
    nome = request.form.get('nome')
    cpf = request.form.get('cpf')
    usuario = Teste(nome=nome, cpf=cpf) #Criando um objeto da classe usuário que será uma nova informação no banco
    db.session.add(usuario) #Adiciona o objeto novo_usuario à sessão do banco de dados, preparando-o para ser salvo
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
    recovery_usuario = Teste.query.get(cpf) #Precisa informar a primary key da tupla. Isso recebe os dados da tupla para essa variável.
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
    usuario = Teste.query.get(cpf)  #Busca um usuário pelo CPF do usuário
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
    usuario = Teste.query.get(cpf)  #Busca um usuário pelo CPF do usuário
    db.session.delete(usuario)
    db.session.commit()
    return render_template("deletado.html", cpf = cpf)