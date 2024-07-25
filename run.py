from config_banco import ConnectDB
from entidades_db import Posts, Users
from crud import CrudDbUsers, CrudDbPosts
from api import ConsomeApi
from decouple import config

#Instancias para manipular o banco e api
usuario = config('USUARIO')
senha = config('SENHA')
host = config('HOST')
banco_nome = config('BANCO')
porta = config('PORTA')
db = ConnectDB(usuario, senha, host, banco_nome, porta)
crud_users = CrudDbUsers(db)
crud_posts = CrudDbPosts(db)
operation_api = ConsomeApi()

def print_users(users):
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Username: {user.username}, Email: {user.email}, Phone: {user.phone}, Website: {user.website}")

def print_posts(posts):
    for post in posts:
        print(f"ID: {post.id}, User ID: {post.user_id}, Title: {post.title}, Body: {post.body}")

if __name__ == "__main__":

    '''operações de obtenção de dados da api e armazenamento no banco de dados, CRUD(Criando, Inserindo, Atualizando e Deletando)'''

    #CREATE 
    users = operation_api.get_users() #dados obtidos de https://jsonplaceholder.typicode.com/users

    for user_data in users: 
        user = Users(
            name=user_data['name'],
            username=user_data['username'],
            email=user_data['email'],
            phone=user_data['phone'],
            website=user_data['website']
        )
        if crud_users.insert_one(user):
            print(f"Usuario:{user.name} foi criado no banco de dados com sucesso, após a obtenção dos dados na API")
        else:
            print(f"Falha interna ao criar o usuario: {user.name}")

    print(100*'-')

    # Obter e inserir posts no banco de dados -> https://jsonplaceholder.typicode.com/posts
    posts = operation_api.get_posts()
    for post_data in posts:
        post = Posts(
            id=post_data['id'],
            user_id=post_data['userId'],
            title=post_data['title'],
            body=post_data['body']
        )
        if crud_posts.insert_one(post):
            print(f'o Post com o titulo: {post.title} foi criado no banco de dados com sucesso, após a obetenção dos dados na API')
        else:
            print(f'ocorreu um erro na criação do Post com o titulo: {post.title}--{crud_posts.insert_one(post)}')
    
    print(100*'-')

    
    #criação de usuário e posts na api https://jsonplaceholder.typicode.com
    #POST
    new_user = {
        "name": "Vinicius",
        "username": "Vinicius INOVA",
        "email": "Vinicius.sales@teste.com",
        "phone": "11-47863-7890",
        "website": "https://vinicius.com"
    }
    created_user = operation_api.create_user(new_user)
    if created_user:
        print("Usuario criado:", created_user)
    else:
        print(f'ocorreu a mensagem:{created_user}')
    
    print(100*'-')

    #posts
    new_post = {
        "userId": created_user['id'],
        "title": "Novo posto",
        "body": "Esse é um novo post"
    }
    created_post = operation_api.create_post(new_post)

    if created_post:
        print("o post foi criado com sucesso:", created_post)
    else:
        print(f'Erro na chamada da API')

    print(100*'-')

    
    #UPDATE user

    #novos dados
    updated_user_data = {
        "name": "fulano",
        "username": "ciclano",
        "email": "fulano.ciclano.@teste.com",
        "phone": "11-9876432",
        "website": "https://fulano.com"
    }
    updated_user = operation_api.update_user(created_user['id'], updated_user_data) #atualizando o usuario vinicius criado acima

    if updated_user:
        print("Usuario Atualizado:", updated_user)
    else:
        print(f'Erro ao chamar a Api')
    
    
    print(100*'-')

    #UPDATE post

    #novos dados
    updated_post_data = {
        "userId": created_user['id'],
        "title": "Updated Post",
        "body": "This is an updated post."
    }
    updated_post = operation_api.update_post(created_post['id'], updated_post_data) #vou atualizar os post criado acima
    if updated_post:
        print("Post atualizado:", updated_post)
    else:
        print('Erro ao chamar a Api:')
    
    print(100*'-')

    
    # Exemplos de patch (atualização parcial) de usuário e post

    #PATCH user
    patch_user_data = {
        "username": "rodrigo caio oliveira"  #atualizarei apenas o username
    }
    patched_user = operation_api.patch_user(created_user['id'], patch_user_data) #atualizando o usuario criado acima

    if patched_user:
        print("Atualização parcial realizada com sucesso:")
    else:
        print(f'erro na chamada da api')
    
    print(100*'-')

    #PATCH post
    patch_post_data = {
        "title": "Patched Post" #atualizarei apenas o title
    }

    patched_post = operation_api.patch_post(created_post['id'], patch_post_data) #atualizando o post criado acima
    if patched_post:
        print("Posto parcialmente atualizado:", patched_post)
    else:
        print(f'ocorreu a mensagem:{patched_post}')
    
    print(100*'-')

    #DELETE de usuário e post

    #user
    delete_user_status = operation_api.delete_user(created_user['id']) #deletando o usuario acima
    if delete_user_status == 200:
        print("Usuario deletado com sucesso, status:", delete_user_status)
    else:
         print("ocorreu o status:", delete_user_status)
    
    print(100*'-')
    
    #post
    delete_post_status = operation_api.delete_post(created_post['id']) #deletando o posto acima

    if delete_post_status == 200:
        print("Post deletado:", delete_post_status)
    else: 
        print("ocorreu o status:", delete_post_status)


    print(100*'-')

    # READ usuarios salvos no banco de dados
    db_users = crud_users.read_all()
    print("Usuários do Banco de Dados:")
    print_users(db_users)

    print(100*'-')

    # READ Posts salvos no banco de dados 
    db_posts = crud_posts.read_all()
    print("Posts do Banco de Dados:")
    print_posts(db_posts)

    print(100*'-')

    # UPDATE usuarios salvos no banco de dados 
    dados_alterar = Posts(title='barbearia')
    print(f'antigo titulo: {db_posts[0].title}')
    db_posts_update = crud_posts.update_one(db_posts[0].id, dados_alterar)
    if db_posts_update:
        print(f"alterado titulo no Banco de Dados com sucesso para {dados_alterar.title}")
    else:
        print('ocorreu um erro ao alterar o titulo no banco')

    print(100*'-')

    # UPDATE Posts salvos no banco de dados 
    dados_alterar = Users(name='Zeca')
    print(f'antigo nome:{db_users[0].name}')
    db_users_update = crud_users.update_one(db_users[0].id, dados_alterar)
    if db_users_update:
        print(f'alterado o name no banco de dados com suceso para {dados_alterar.name}')
    else:
        print(f'ocoreu um erro ao tentr alterar o nome no banco')

    print(100*'-')


    # DELETE Posts salvos no banco de dados 
    print(f'o poste de titulo: {db_posts[0].title} sera apagado')
    db_posts = crud_posts.delete_one(db_posts[0].id)
    if db_posts:
        print("poste apagado com sucesso no banco de dados")
    else:
        print('ocorreu um erro ao deletar esse poste no banco')

    print(100*'-')

    #DELETE Usuarios salvos no banco
    print(f'o usuario de nome: {db_users[0].name} sera apagado')
    db_posts = crud_users.delete_one(db_users[0].id)
    if db_posts:
        print("usuario apagado do banco de dados com sucesso")
    else:
        print('ocorreu um erro ao apagar o usuario do banco de dados')












    # Users operacoes CRUD 
    #print("todos os usuarios: ")
    #users = crud_users.read_all()
    #print_users(users)

    #print("\nInserindo um novo usuario:")
    #if crud_users.insert_one(user_3):
    #    print("Usuario criado com sucesso")
    #else:
    #   print("Falha interna ao criar o usuario")


    #print("\nInserindo varios usuarios:")
    #if crud_users.insert_more_than_one(users):
    #    print('Usuarios inseridos com sucesso')
    #else:
    #   print("Falha ao inserir usuarios")

    #print("\n Ver 1 ou mais usuarios exemplo = (name='julio' OR id=1):")
    #users = crud_users.read_one_or_more(name='julio', id=1)
    #print_users(users)

    #print("\nAualizando um usuario (id=1):")
    #if crud_users.update_one(id=1, dados_atualizar=user_1_update):
    #   print("Usuario atualizado com sucesso")
    #else:
     #   print("Falha ao atualizar Usuario")

    #print("\nDeletando o usuario (id=1):")
    #if crud_users.delete_one(id=1):
    #    print("Usuario deletado com sucesso")
    #else:
    #    print("Failed to delete user")




    # Posts oepracoes CRUD 
    #print("\nLista deTodos os Posts:")
    #posts = crud_posts.read_all()
    #print_posts(posts)

    #print("\nInserir um novo post:")
    #if crud_posts.insert_one(post_1):
    #    print("Post inserido com sucesso")
    #else:
    #    print("ocorreu um erro interno ao inserir post")

    #print("\nInserindo varios posts:")
    #if crud_posts.insert_more_than_one(posts):
    #    print("Posts inseridos com sucessos")
    #else:
    #    print("Falha ao inserir posts")

    #print("\nLista de 1 ou mais posts (user_id=2):")
    #posts = crud_posts.read_one_or_more(user_id=2)
    #print_posts(posts)

    #print("\nAtualizando o post (id=1):")
    #if crud_posts.update_one(id=1, dados_atualizar=post_2):
    #    print("Post atualizado com sucesso")
    #else:
    #    print("Falha ao atualizar o post")

    #print("\nPost deletado - (id=1):")
    #if crud_posts.delete_one(id=1):
    #    print("Post deletado com sucesso")
    #else:
    #    print("ocorreu um erro interno ao deletar o post")

