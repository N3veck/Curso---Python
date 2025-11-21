from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Garantia:
    """
    Cobertura de garantia para um equipamento (histórico possível).
    """
    id_garantia: int
    id_usuario: int
    id_equipamento: int
    data_inicio: date
    data_fim: date
    tipo_garantia: Optional[str] = None   # 'fabricante', 'estendida', etc.

    def __str__(self) -> str:
        return f"Garantia {self.tipo_garantia or 'padrão'}: {self.data_inicio} → {self.data_fim}"
