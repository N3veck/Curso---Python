from dataclasses import dataclass
from typing import Optional

@dataclass
class Loja:
    """
    Loja cadastrada por um usuário.
    """
    id_loja: int
    id_usuario: int
    nome: str
    cnpj: Optional[str] = None
    endereco: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None

    def __str__(self) -> str:
        return f"Loja {self.nome} (id={self.id_loja})"
