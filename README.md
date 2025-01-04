# Anotações

    AQUI ESTÃO ALGUMAS DICAS E INSTRUÇÕES GERAIS SOBRE OS TEMAS QUE ABORDAMOS NESSE PROJETO

--------------------------------------------------------------------------------------------------------------------

Para comunicar com um banco de dados precisamos de alguns passos:

• Criação de um arquivo.flaskenv

• Instalar as seguintes dependências:

    • pip install pymysql - Necessário para conectar ao banco

    • pip install flask_sqlalchemy - Pacote com as informações necessárias para manuserio de um banco mysql

    • pip install python-dotenv - Pacote para fazer com que as informações do arquivo.flaskenv sejam carregados

• Para criar arquivo com as dependências:
    • Execute o código: pip freeze > requirements.txt

• Para instalar as dependências ao criar um novo codespace:
    • Execute o código: pip install -r requirements.txt


-------------------------------------------------------------------------

                    INSTALAÇÃO DO LOGIN MANAGER

• Para utilizar o login_manager precisamos instalar a dependência flask-login

• Em Utilidades, vamos instancias o login manager

• Em Models precisamos criar um modelo de classe para o nosso usuário 
    • Essa classe precisará ter a função >get_id< que é o nome padrão da função que será usado no login manager

• Por falar em funções, precisamos configurar o @lm.user_loader no app.py. Ela será responsável pela função de buscar um usuário no banco

• login_user(usuario) e logout_user() São utilizadas quando precisamos iniciar e encerrar uma sessão do usuário

• @login_required sinaliza que aquela rota está "protegida", necessitando obrigatoriamente de um login