
import sqlite3

# Função para criar a tabela de usuários no banco de dados SQLite
def create_user_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Criar a tabela de usuários antes de executar o servidor
create_user_table()

def add_user(username, password):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()

        return True
    except Exception as e:
        print(f"Erro ao adicionar usuário: {e}")
        return False
    
# Exemplo de uso:
if __name__ == '__main__':
    username = 'junior'
    password = '1234'

    if add_user(username, password):
        print(f"Usuário '{username}' adicionado com sucesso!")
    else:
        print(f"Erro ao adicionar usuário '{username}'.")