class Livro:
    """Livro."""

    def __init__(self, codigo, titulo, autor, ano):
        """Init."""
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def marcar_como_emprestado(self):
        """Emprestar."""
        if not self.disponivel:
            return False
        self.disponivel = False
        return True

    def marcar_como_devolvido(self):
        """Devolver."""
        self.disponivel = True

    def esta_disponivel(self):
        """Disponível?"""
        return self.disponivel

    def __repr__(self):
        """Resumo."""
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.codigo} - {self.titulo} ({self.autor}, {self.ano}) - {status}"
