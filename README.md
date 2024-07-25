# desafio_tecnico_inove
Desafio técnico da Inove - desenvolvedor python web

para rodar o projeto primeiro de um git clone https://github.com/VsSalles/desafio_tecnico_inove.git

após isso instale as bibliotecas com o comando pip install requirements.txt

após isso crie um ambiente virtual com o comando python -m venv venv

ative o ambiente virtual com o comando venv/scripts/activate.ps1

instale as bibliotecas com o comando pip install -r requirements.txt

para o banco de dados você tera que inserir as credencias no arquivo na instancia db = ConnectDB('usuario', 'senha', 'host', 'banco_name', port),nos arquivos entidades_db.py e run.py

após rode uma vez o comando python entidades_db.py para a criação das tabelas

por fim rode o arquivo run.py onde tem as operações no banco de dados e api

Desafio realizado com as bibliotecas SqlAlchemy, Requests e psycopg2


Api.py = responsavel por fazer todas as requisições a Api

config_banco = todas as configurações do banco, engine e session

entidades_db.py = a representação das tabelas post e usuarios no banco

crud = Operações de criação, leitura, atualização e deleção no banco

run.py = arquivo que executa tudo

Vinicius Sales Santana
