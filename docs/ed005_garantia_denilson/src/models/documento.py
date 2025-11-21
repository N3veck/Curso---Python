from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Documento:
    """
    Documento associado a pelo menos um contexto (loja/equipamento/garantia).
    """
    id_documento: int
    id_usuario: int
    url: str
    tipo_doc: str                 # 'nota_fiscal', 'certificado', 'termo', ...
    num_doc: Optional[str] = None
    data_emissao: Optional[date] = None
    id_loja: Optional[int] = None
    id_equipamento: Optional[int] = None
    id_garantia: Optional[int] = None

    def __str__(self) -> str:
        ctx = ["loja" if self.id_loja else None,
               "equip" if self.id_equipamento else None,
               "garantia" if self.id_garantia else None]
        ctx = "/".join([c for c in ctx if c])
        return f"{self.tipo_doc.upper()} {self.num_doc or ''} ({ctx or 'sem-contexto'})".strip()
