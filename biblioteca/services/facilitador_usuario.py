class FacilitadorUsuario:
    """Usuários."""

    def __init__(self):
        """Init."""
        self.cadastrados = []

    def adicionar_usuario(self, nome, id_usuario):
        """Adicionar."""
        novo = Usuario(nome, id_usuario)
        self.cadastrados.append(novo)
        return novo

    def listar_todos(self):
        """Listar."""
        return self.cadastrados

    def buscar_por_id(self, id_usuario):
        """Buscar."""
        for u in self.cadastrados:
            if u.id_usuario == id_usuario:
                return u
        return None