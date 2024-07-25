from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ConnectDB:
    def __init__(self, usuario: str, senha: str, host: str, banco_nome: str, porta: int, banco='postgresql', lib='psycopg2') -> None:
        self.usuario = usuario
        self.senha = senha
        self.host = host
        self.banco_nome = banco_nome
        self.porta = porta
        self.banco = banco
        self.lib = lib
        
    def __connect_engine(self):
        self.string_conexao = f'{self.banco}+{self.lib}://{self.usuario}:{self.senha}@{self.host}:{self.porta}/{self.banco_nome}'
        self.engine = create_engine(self.string_conexao, echo=False)
        return self.engine
    
    def __session(self):
        self.Session = sessionmaker(bind=self.get_engine())
        return self.Session()

    def get_engine(self):
        return self.__connect_engine()
    
    def get_session(self):
        return self.__session()
    

    


    

    