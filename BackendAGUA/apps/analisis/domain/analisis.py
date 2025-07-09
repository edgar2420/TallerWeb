from dataclasses import dataclass
from datetime import date

@dataclass
class Analisis:
    id: int
    salida_campo_id: int
    fecha_analisis: date
    parametro: str
    valor: float
    unidad: str
    observaciones: str
