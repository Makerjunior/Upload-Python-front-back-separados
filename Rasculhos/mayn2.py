import os
import sqlite3
from flask import Flask, request, send_from_directory, render_template, request, jsonify
from file_list_utils import get_file_list
from image_gallery_utils import get_image_gallery

app = Flask(__name__)

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


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

@app.route('/upload', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST':
    file = request.files['file']
    file.save(os.path.join('arquivos', file.filename))
    return f'Arquivo "{file.filename}" carregado com sucesso! <a href="/">Voltar</a>'
  else:
    file_list = get_file_list()
    image_gallery = get_image_gallery()
    return render_template('index.html',
                           file_list=file_list,
                           image_gallery=image_gallery)

@app.route('/arquivos/<filename>')
def download(filename):
  return send_from_directory('./arquivos', filename)

@app.route('/')
def form():
  return render_template('login.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
