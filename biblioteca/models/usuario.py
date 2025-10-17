class Usuario:
    """Usuário da biblioteca."""

    def __init__(self, id_usuario, nome):
        """Init."""
        self.id_usuario = id_usuario
        self.nome = nome
        self.livros = []

    def pegar_emprestado(self, livro):
        """Emprestar livro."""
        if livro.marcar_como_emprestado():
            self.livros.append(livro)
            return True
        return False

    def devolver_livro(self, livro):
        """Devolver livro."""
        if livro in self.livros:
            livro.marcar_como_devolvido()
            self.livros.remove(livro)
            return True
        return False

    def __repr__(self):
        """Resumo."""
        return f"{self.id_usuario} - {self.nome}"
