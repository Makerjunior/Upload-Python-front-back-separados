
class User:
    logged_in_user = None  # variável global para armazenar o usuário logado

    def login(self, username, password):
        user = self.get_user(username)
        if user and user[2] == password:  # verificação de senha
            self.logged_in_user = user[1]  # armazena o nome do usuário logado
            return True
        else:
            return False

    def get_logged_in_user(self):
        return self.logged_in_user

#####################
# Criando um objeto User
'''
user_obj = User()
nome="junior"
senha="12234"
# Fazendo login com um usuário válido
if user_obj.login(nome, senha):
    print("Login bem-sucedido!")
else:
    print("Login falhou!")

# Recuperando o usuário atualmente logado
logged_in_user = user_obj.get_logged_in_user()
if logged_in_user:
    print("Usuário logado:", logged_in_user)
else:
    print("Nenhum usuário logado.")
'''