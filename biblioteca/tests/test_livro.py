from src.models.livro import Livro

def test_livro():
    """Livro."""
    # criar livro
    l = Livro("O Hobbit", "J.R.R. Tolkien", 1937, "L020")
    
    # emprestar
    assert l.emprestar() is True
    assert l.disponivel is False
    
    # devolver
    l.devolver()
    assert l.disponivel is True
