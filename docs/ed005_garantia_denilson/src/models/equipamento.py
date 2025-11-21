from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Equipamento:
    """
    Item comprado em uma loja (pertence a uma loja e a um usuário).
    """
    id_equipamento: int
    id_usuario: int
    id_loja: int
    produto: str
    numero_serie: str
    data_compra: date
    preco: float
    marca: Optional[str] = None
    modelo: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.produto} (NS: {self.numero_serie}) — {self.data_compra}"
