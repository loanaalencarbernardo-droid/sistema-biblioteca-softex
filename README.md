# sistema-biblioteca-softex
Aplicação desenvolvida em Python para o controle de uma biblioteca, estruturada com base nos conceitos de Programação Orientada a Objetos (POO) e nas Boas Práticas de Engenharia de Software. O projeto tem como foco a organização do código, reutilização de componentes e aprimoramento do aprendizado.

##  Objetivo do Projeto

Criar um sistema capaz de:

- Cadastrar livros e usuários
- Registrar empréstimos e devoluções
- Listar informações de forma organizada

O projeto utiliza:

- Classes e objetos (POO)
- Encapsulamento e modularização
- Testes automatizados com pytest
- Estrutura de projeto limpa e bem documentada

##  Estrutura do Projeto

biblioteca/
│
├── src/
│ ├── init.py
│ ├── main.py
│ ├── utils.py
│ │
│ ├── models/
│ │ ├── init.py
│ │ ├── emprestimo.py
│ │ ├── livro.py
│ │ └── usuario.py
│ │
│ ├── services/
│ │ ├── init.py
│ │ ├── gerenciador_emprestimos.py
│ │ ├── gerenciador_livros.py
│ │ └── gerenciador_usuarios.py
│ │
│ └── tests/
│ ├── init.py
│ ├── test_emprestimo.py
│ ├── test_livro.py
│ └── test_usuario.py
│
├── requirements.txt
└── README.md


##  Tecnologias e Conceitos Utilizados

- Python 3
- Programação Orientada a Objetos (POO)
- Modularização de código
- Testes automatizados (pytest)
- Boas práticas de documentação
- Código limpo com estrutura simplificada tipo MVC


##  Criadora do Projeto

Loana Alencar 
✉️ loana.alencarbernardo@hotmail.com

💡 Este sistema foi desenvolvido como projeto didático para estudo e prática de Python e POO.
