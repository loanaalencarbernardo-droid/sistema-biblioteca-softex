from services.gerenciador_livros import GerenciadorLivros
from services.gerenciador_usuarios import GerenciadorUsuarios
from services.gerenciador_emprestimos import GerenciadorEmprestimos
from utils import exibir_menu

def cadastrar_livro(livros, usuarios, emprestimos):
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    codigo = input("Código: ")
    livro = livros.cadastrar_livro(titulo, autor, ano, codigo)
    print(f"\nLivro registrado: {livro}")

def cadastrar_usuario(livros, usuarios, emprestimos):
    nome = input("Nome: ")
    id_usuario = input("ID: ")
    usuario = usuarios.cadastrar_usuario(nome, id_usuario)
    print(f"\nUsuário registrado: {usuario}")

def listar_livros(livros, usuarios, emprestimos):
    print("\nLista de livros:")
    for l in livros.listar_livros():
        print(l)

def listar_usuarios(livros, usuarios, emprestimos):
    print("\nLista de usuários:")
    for u in usuarios.listar_usuarios():
        print(u)

def registrar_emprestimo(livros, usuarios, emprestimos):
    processar_emprestimo(livros, usuarios, emprestimos, "registrar")

def finalizar_emprestimo(livros, usuarios, emprestimos):
    processar_emprestimo(livros, usuarios, emprestimos, "finalizar")

def listar_emprestimos(livros, usuarios, emprestimos):
    print("\nEmpréstimos atuais:")
    for e in emprestimos.listar_emprestimos():
        print(e)

def sair(livros, usuarios, emprestimos):
    print("\nSistema encerrado. Até mais!")
    exit()

def processar_emprestimo(livros, usuarios, emprestimos, acao):
    id_usuario = input("ID do usuário: ")
    codigo = input("Código do livro: ")
    usuario = usuarios.buscar_usuario(id_usuario)
    livro = livros.buscar_livro(codigo)

    if not usuario or not livro:
        print("\nUsuário ou livro não encontrado.")
        return

    if acao == "registrar":
        if emprestimos.registrar_emprestimo(usuario, livro):
            print("\nEmpréstimo realizado com sucesso!")
        else:
            print("\nEste livro já está emprestado.")
    else:
        if emprestimos.finalizar_emprestimo(usuario, livro):
            print("\nLivro devolvido com sucesso!")
        else:
            print("\nEmpréstimo não encontrado.")

def main():
    livros = GerenciadorLivros()
    usuarios = GerenciadorUsuarios()
    emprestimos = GerenciadorEmprestimos()

    acoes = {
        "1": cadastrar_livro,
        "2": cadastrar_usuario,
        "3": listar_livros,
        "4": listar_usuarios,
        "5": registrar_emprestimo,
        "6": finalizar_emprestimo,
        "7": listar_emprestimos,
        "0": sair
    }

    while True:
        escolha = exibir_menu()
        acao = acoes.get(escolha)
        if acao:
            acao(livros, usuarios, emprestimos)
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
