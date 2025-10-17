class FacilitadorEmprestimo:
    """Empréstimos."""

    def __init__(self):
        """Init."""
        self.ativos = []

    def criar_emprestimo(self, usuario, livro):
        """Criar."""
        e = Emprestimo(usuario, livro)
        sucesso = e.registrar()
        if sucesso:
            self.ativos.append(e)
        return sucesso

    def concluir_emprestimo(self, usuario, livro):
        """Concluir."""
        for e in self.ativos:
            if e.usuario == usuario and e.livro == livro and not e.data_devolucao:
                e.finalizar()
                return True
        return False

    def obter_emprestimos(self):
        """Listar."""
        return self.ativos
