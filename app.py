from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'segredo'

def conectar():
    return sqlite3.connect('banco.db')

def init_db():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

init_db()

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        senha = request.form['senha']

        if username == '' or senha == '':
            return "Campos vazios"

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            'INSERT INTO usuarios (username, senha) VALUES (?, ?)',
            (username, senha)
        )

        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        senha = request.form['senha']

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            'SELECT * FROM usuarios WHERE username=? AND senha=?',
            (username, senha)
        )

        usuario = cursor.fetchone()

        conn.close()

        if usuario:
            session['usuario'] = username
            return redirect(url_for('tarefas_lista'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))