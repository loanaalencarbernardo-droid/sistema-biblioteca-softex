class FacilitadorLivro:
    """Livros."""

    def __init__(self):
        """Init."""
        self.acervo = []

    def adicionar_livro(self, titulo, autor, ano, codigo):
        """Adicionar."""
        novo = Livro(titulo, autor, ano, codigo)
        self.acervo.append(novo)
        return novo

    def listar_todos(self):
        """Listar."""
        return self.acervo

    def buscar_por_codigo(self, codigo):
        """Buscar."""
        for l in self.acervo:
            if l.codigo == codigo:
                return l
        return None