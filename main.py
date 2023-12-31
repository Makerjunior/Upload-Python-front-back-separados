import os
from flask import Flask, request, send_from_directory, render_template, request, jsonify
from file_list_utils import get_file_list
from image_gallery_utils import get_image_gallery
from database import UserDatabase  # Importe a classe UserDatabase do arquivo database.py
from User import User
app = Flask(__name__)



user_db = UserDatabase()
user_db.add_user("junior",'castevania')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user_db = UserDatabase()
 
    user = user_db.get_user(username)



    if user and user[2] == password:  # O índice 2 corresponde à coluna "password" na tabela
      file_list = get_file_list()
      image_gallery = get_image_gallery()
      print(user_db.get_all_users())
      return render_template('index.html',
                           file_list=file_list,
                           image_gallery=image_gallery)
    else:
         return render_template('erro.html')

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

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join('arquivos', file.filename))
        file_list = get_file_list()
        image_gallery = get_image_gallery()
        return render_template('index.html',
                           file_list=file_list,
                           image_gallery=image_gallery)
    else:
        return jsonify({'message': 'Envie um arquivo usando POST.'})

# Mantenha a rota original para a página de upload
@app.route('/arquivos', methods=['GET'])
def upload_page():
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
    app.run(host='0.0.0.0', port=5000)
