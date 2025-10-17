def exibir_menu():
    opcoes = {
        "1": "Adicionar livro",
        "2": "Adicionar usuário",
        "3": "Mostrar livros",
        "4": "Mostrar usuários",
        "5": "Realizar empréstimo",
        "6": "Registrar devolução",
        "7": "Listar todos os empréstimos",
        "0": "Encerrar sistema"
    }

    print("\n===== MENU DO SISTEMA DE BIBLIOTECA =====")
    for chave, descricao in opcoes.items():
        print(f"{chave} - {descricao}")

    return input("Digite sua escolha: ")
