from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    """
    Representa o dono dos dados (escopo multi-tenant).
    """
    id_usuario: int
    nome: str
    email: Optional[str] = None
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    status: str = "ativo"     # 'ativo' | 'inativo'

    def __str__(self) -> str:
        return f"{self.nome} <{self.email or 'sem-email'}> [{self.status}]"
