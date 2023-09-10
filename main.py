import os
from flask import Flask, request, send_from_directory, render_template, request, jsonify
from file_list_utils import get_file_list
from image_gallery_utils import get_image_gallery

# Simulação de um banco de dados de usuários (substitua pelo seu banco de dados real)
users = {
    'usuario1': 'senha1',
    'usuario2': 'senha2',
}

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if username in users and users[username] == password:
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


#ngrok http 80 --region=us --header="ngrok-skip-browser-warning: true"