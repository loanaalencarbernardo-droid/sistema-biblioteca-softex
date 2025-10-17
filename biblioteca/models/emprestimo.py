class Emprestimo:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro
        self.data_inicio = None
        self.data_fim = None

    def iniciar_emprestimo(self):
        if not self.livro.disponivel:
            return False
        self.livro.disponivel = False
        self.usuario.livros.append(self.livro)
        return True

    def encerrar_emprestimo(self):
        if self.livro in self.usuario.livros:
            self.livro.disponivel = True
            self.usuario.livros.remove(self.livro)
            return True
        return False

    def __str__(self):
        status = "Em andamento" if not self.data_fim else "Devolvido"
        return f"{self.usuario.nome} - {self.livro.titulo} ({status})"


