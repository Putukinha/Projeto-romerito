from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados em memória
usuarios = []
tarefas = []

# AUTENTICAÇÃO (SEM SESSION)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        senha = request.form['senha']

        for u in usuarios:
            if u['username'] == username and u['senha'] == senha:
                return redirect(url_for('tarefas_lista'))

    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuarios.append({
            'username': request.form['username'],
            'senha': request.form['senha']
        })
        return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# CRUD DE TAREFAS

@app.route('/tarefas')
def tarefas_lista():

    filtro = request.args.get('status')

    if filtro == 'concluida':
        lista = [t for t in tarefas if t['status'] == 'concluida']
    elif filtro == 'pendente':
        lista = [t for t in tarefas if t['status'] == 'pendente']
    else:
        lista = tarefas

    return render_template('tarefas.html', tarefas=lista)

@app.route('/nova', methods=['POST'])
def nova_tarefa():
    tarefas.append({
        'id': len(tarefas),
        'titulo': request.form['titulo'],
        'status': 'pendente'
    })
    return redirect(url_for('tarefas_lista'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarefa = tarefas[id]

    if request.method == 'POST':
        tarefa['titulo'] = request.form['titulo']
        tarefa['status'] = request.form['status']
        return redirect(url_for('tarefas_lista'))

    return render_template('editar.html', tarefa=tarefa)

@app.route('/deletar/<int:id>')
def deletar(id):
    tarefas.pop(id)
    return redirect(url_for('tarefas_lista'))


if __name__ == '__main__':
    app.run(debug=True)

