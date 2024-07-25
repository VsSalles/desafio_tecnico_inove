from sqlalchemy import or_
from config_banco import ConnectDB
from entidades_db import Users, Posts

class CrudDbUsers:
    def __init__(self, connection_db: ConnectDB) -> None:
        self.session = connection_db.get_session()

    # Ler (SELECT) todos os registros da tabela users
    def read_all(self):
        try:
            return self.session.query(Users).all()
        except Exception as e:
            print(e)
            return False

    # Ler (SELECT) apenas um ou mais registros da tabela users
    def read_one_or_more(self, id=None, name=None, email=None, phone=None, website=None) -> list:
        try:
            conditions = []
            if id:
                conditions.append(Users.id == id)
            if name:
                conditions.append(Users.name == name)
            if email:
                conditions.append(Users.email == email)
            if phone:
                conditions.append(Users.phone == phone)
            if website:
                conditions.append(Users.website == website)

            query = self.session.query(Users)
            if conditions:
                query = query.filter(or_(*conditions))

            return query.all()
        except Exception as e:
            print(e)
            return False

    # Criar apenas um registro
    def insert_one(self, usuario: Users) -> bool:
        try:
            self.session.add(usuario)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    # Criar mais de um registro
    def insert_more_than_one(self, usuarios: list[Users]) -> bool:
        try:
            self.session.add_all(usuarios)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    # Atualizar um único registro, é possível atualizar um único valor da coluna ou o registro inteiro
    def update_one(self, id, dados_atualizar: Users) -> bool:
        try:
            user = self.session.query(Users).filter(Users.id == id).one()
            user.name = dados_atualizar.name
            user.username = dados_atualizar.username
            user.email = dados_atualizar.email
            user.phone = dados_atualizar.phone
            user.website = dados_atualizar.website
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    # Deletar um único registro
    def delete_one(self, id) -> bool:
        try:
            user = self.session.query(Users).filter(Users.id == id).one()
            self.session.delete(user)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False


class CrudDbPosts:
    def __init__(self, connection_db: ConnectDB) -> None:
        self.session = connection_db.get_session()

    # Ler (SELECT) todos os registros da tabela posts
    def read_all(self):
        try:
            return self.session.query(Posts).all()
        except Exception as e:
            self.session.rollback()
            return False

    # Ler (SELECT) um ou mais registros da tabela posts
    def read_one_or_more(self, id=None, user_id=None, title=None, body=None) -> list:
        try:
            conditions = []
            if id:
                conditions.append(Posts.id == id)
            if user_id:
                conditions.append(Posts.user_id == user_id)
            if title:
                conditions.append(Posts.title == title)
            if body:
                conditions.append(Posts.body == body)

            query = self.session.query(Posts)
            if conditions:
                query = query.filter(or_(*conditions))

            return query.all()
        except Exception as e:
            self.session.rollback()
            return False

    # Criar (INSERT) apenas um registro
    def insert_one(self, post: Posts) -> bool:
        try:
            self.session.add(post)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    # Criar (INSERT) mais de um registro
    def insert_more_than_one(self, posts: list[Posts]) -> bool:
        try:
            self.session.add_all(posts)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    # Atualizar um único registro
    def update_one(self, id, dados_atualizar: Posts) -> bool:
        try:
            post = self.session.query(Posts).filter(Posts.id == id).one()
            post.user_id = dados_atualizar.user_id
            post.title = dados_atualizar.title
            post.body = dados_atualizar.body
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    # Deletar um único registro
    def delete_one(self, id) -> bool:
        try:
            post = self.session.query(Posts).filter(Posts.id == id).one()
            self.session.delete(post)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

