from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from config_banco import ConnectDB
from decouple import config

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    username = Column(String(255))
    email = Column(String(255))
    phone = Column(String(255))
    website = Column(String(255))

class Posts(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String(255))
    body = Column(String)

if __name__ == "__main__":
    usuario = config('USUARIO')
    senha = config('SENHA')
    host = config('HOST')
    banco_nome = config('BANCO')
    porta = config('PORTA')
    db = ConnectDB(usuario, senha, host, banco_nome, porta)
    
    Base.metadata.create_all(bind=db.get_engine())