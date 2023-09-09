import os
from flask import Flask, request, send_from_directory, render_template
from file_list_utils import get_file_list
from image_gallery_utils import get_image_gallery

app = Flask(__name__)


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
def login():
  return render_template('login.html')

@app.route('/pagina')
def php():
  return render_template('index.php')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)


#ngrok http 80 --region=us --header="ngrok-skip-browser-warning: true"