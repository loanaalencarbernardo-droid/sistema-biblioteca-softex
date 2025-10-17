import usuario as usr
import livro as lb

def test_usuario_empresta():
    """Usuário empresta livro."""
    # criar usuário e livro
    u = usr.Usuario("Mariana", "U20")
    l = lb.Livro("O Morro dos Ventos Uivantes", "Emily Brontë", 1847, "L030")
    
    # emprestar
    u.emprestar_livro(l)
    
    # verificar
    assert l.disponivel is False
    assert l in u.livros_emprestados
