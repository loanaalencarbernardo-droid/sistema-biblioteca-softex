from src.models.emprestimo import Emprestimo
from src.models.livro import Livro
from src.models.usuario import Usuario

def test_emprestimo():
    """Teste empréstimo."""
    # criar usuário e livro
    u = Usuario("Carlos", "U10")
    l = Livro("O Pequeno Príncipe", "Saint-Exupéry", 1943, "L010")
    
    # criar empréstimo
    e = Emprestimo(u, l)
    
    # registrar
    sucesso = e.registrar()
    
    # verificar
    assert sucesso is True
    assert l.disponivel is False
