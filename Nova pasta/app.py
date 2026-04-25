from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

usuarios = []
tarefas = []
contador_id = 0 

def encontrar_tarefa(id):
    for t in tarefas:
        if t['id'] == id:
            return t
    return None

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
    global contador_id

    tarefas.append({
        'id': contador_id,
        'titulo': request.form['titulo'],
        'status': 'pendente'
    })

    contador_id += 1
    return redirect(url_for('tarefas_lista'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarefa = encontrar_tarefa(id)

    if not tarefa:
        return "Tarefa não encontrada"

    if request.method == 'POST':
        tarefa['titulo'] = request.form['titulo']
        tarefa['status'] = request.form['status']
        return redirect(url_for('tarefas_lista'))

    return render_template('editar.html', tarefa=tarefa)

@app.route('/deletar/<int:id>')
def deletar(id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != id]
    return redirect(url_for('tarefas_lista'))

if _name_ == '_main_':
    app.run(debug=True)
