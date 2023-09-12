import sqlite3
class UserDatabase:
    def __init__(self):
        conn = sqlite3.connect('db/users.db')
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

    def add_user(self, username, password):
        try:
            conn = sqlite3.connect('db/users.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Erro ao adicionar usuário: {e}")
            return False

    def get_user(self, username):
        try:
            conn = sqlite3.connect('db/users.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            conn.close()
            return user
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None

    def update_user(self, username, new_password):
        try:
            conn = sqlite3.connect('db/users.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            return False

    def delete_user(self, username):
        try:
            conn = sqlite3.connect('db/users.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE username = ?', (username,))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            return False

    def get_all_users(self):
        try:
            conn = sqlite3.connect('db/users.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            conn.close()
            return users
        except Exception as e:
            print(f"Erro ao buscar todos os usuários: {e}")
            return None
