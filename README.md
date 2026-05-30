# Projeto-romerito

Este projeto consiste em uma aplicação web desenvolvida com Flask para auxiliar no gerenciamento de tarefas. O sistema permite que usuários criem uma conta, realizem login e organizem suas atividades de forma simples e prática. As informações são armazenadas em um banco de dados SQLite3, garantindo que os dados permaneçam salvos mesmo após o encerramento da aplicação.

Funcionalidades:

Cadastro de usuários
Login e logout
Controle de acesso por sessão
Cadastro de tarefas
Listagem de tarefas
Edição de tarefas
Exclusão de tarefas
Filtro de tarefas por status (pendente ou concluída)

Tecnologias Utilizadas:

Python
Flask
SQLite3
HTML
CSS

Como Executar o Projeto:

Instalar o Flask:

pip install flask

Executar a aplicação:
python app.py

Abrir no navegador:
http://127.0.0.1:5000


Estrutura do Projeto:

projeto/
├── app.py
├── banco.db
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── cadastro.html
│   ├── tarefas.html
│   └── editar.html
└── README.md


Banco de Dados:

O projeto utiliza SQLite3 para armazenar os dados dos usuários e das tarefas. Foram criadas duas tabelas principais: uma para os usuários cadastrados e outra para as tarefas. Dessa forma, todas as informações permanecem salvas no sistema mesmo após reiniciar a aplicação.

Sessões:

As sessões foram utilizadas para controlar a autenticação dos usuários. Após realizar o login, o usuário tem acesso às funcionalidades do sistema. Caso não esteja autenticado, o acesso às páginas de gerenciamento de tarefas é bloqueado e o usuário é redirecionado para a tela de login.

Objetivo do Projeto:

O objetivo deste projeto é aplicar os conceitos estudados na disciplina, utilizando Flask, rotas, formulários, sessões e banco de dados SQLite3 para desenvolver uma aplicação web funcional e organizada.

Repositório:

Link do GitHub:(https://github.com/Putukinha/Projeto-romerito.git)
