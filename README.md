# testebd
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