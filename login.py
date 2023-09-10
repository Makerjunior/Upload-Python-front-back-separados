from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados de usuários (substitua pelo seu banco de dados real)
users = {
    'usuario1': 'senha1',
    'usuario2': 'senha2',
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if username in users and users[username] == password:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run(debug=True)