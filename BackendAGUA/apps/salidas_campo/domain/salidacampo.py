from dataclasses import dataclass
from datetime import date

@dataclass
class SalidaCampo:
    id: int
    fecha: date
    responsable: str
    observaciones: str
    localidad_id: int
