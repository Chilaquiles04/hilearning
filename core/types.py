"""
Definición de tipos inmutables del dominio para Hi Learning.
Paradigma: Programación Funcional (Inmutabilidad con frozen=True).
"""

from dataclasses import dataclass
from typing import Tuple, Optional


@dataclass(frozen=True)
class Turno:
    """Representa un turno individual de conversación inmutable."""
    emisor: str            # 'user' o 'assistant'
    texto: str             # Contenido textual del mensaje
    timestamp: float       # Epoch timestamp del turno
    duracion_segundos: float = 0.0


@dataclass(frozen=True)
class MetricasTurno:
    """Métricas funcionales calculadas para un turno del usuario."""
    total_palabras: int
    duracion_segundos: float
    palabras_por_minuto: float
    palabras_unicas: Tuple[str, ...]


@dataclass(frozen=True)
class ReporteFinal:
    """Reporte estructurado generado al finalizar la micro-sesión."""
    total_turnos_usuario: int
    total_palabras: int
    ppm_promedio: float
    vocabulario_utilizado: Tuple[str, ...]
    feedback_gramatical: Tuple[str, ...]
    sugerencias_mejora: Tuple[str, ...]
    calificacion_general: str  # 'Beginner', 'Intermediate', 'Advanced'
