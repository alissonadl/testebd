from flask_sqlalchemy import SQLAlchemy #Biblioteca necessária para mapear classes Python para tabelas do banco de dados relacional
from flask_login import LoginManager, login_user, logout_user, login_required

db = SQLAlchemy() #Instanciando o SQLAlchemy
lm = LoginManager() #Instanciando o LoginManager
