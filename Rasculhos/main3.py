import os
from flask import Flask, request, send_from_directory, render_template, request, jsonify
from file_list_utils import get_file_list
from image_gallery_utils import get_image_gallery
from db.database import UserDatabase  # Importe a classe UserDatabase do arquivo database.py

app = Flask(__name__)

# Resto do seu código permanece inalterado

if __name__ == '__main__':
    username = 'junior'
    password = '1234'

    user_db = UserDatabase()
    if user_db.add_user(username, password):
        print(f"Usuário '{username}' adicionado com sucesso!")
    else:
        print(f"Erro ao adicionar usuário '{username}'.")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user_db = UserDatabase()
    user = user_db.get_user(username)

    if user and user[2] == password:  # O índice 2 corresponde à coluna "password" na tabela
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None  # Inicialmente, não há mensagem para exibir

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if user_db.add_user(username, password):
            message = "Registro bem-sucedido!"
        else:
            message = "Erro no registro."

    return render_template('login.html', message=message)


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

@app.route('/adicionar')
def ad():
    return render_template('adicionar.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
