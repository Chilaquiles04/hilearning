"""
Núcleo Funcional de Análisis y Métricas para Hi Learning.
Todas las funciones son puras (sin efectos secundarios, sin mutación de estado).
Alineado con los requerimientos de la materia de Programación Funcional.
"""

import re
from typing import Tuple, List
from functools import reduce
from core.types import Turno, MetricasTurno, ReporteFinal


def limpiar_y_tokenizar(texto: str) -> Tuple[str, ...]:
    """
    Función pura que extrae palabras en minúsculas ignorando puntuación.
    """
    if not texto:
        return ()
    palabras = re.findall(r"\b[a-zA-Z']+\b", texto.lower())
    return tuple(palabras)


def calcular_ppm(total_palabras: int, duracion_segundos: float) -> float:
    """
    Función pura para calcular palabras por minuto (PPM).
    """
    if duracion_segundos <= 0 or total_palabras <= 0:
        return 0.0
    return round((total_palabras / duracion_segundos) * 60.0, 2)


def analizar_turno_usuario(texto: str, duracion_segundos: float = 5.0) -> MetricasTurno:
    """
    Función pura que toma el texto de un turno y calcula sus métricas individuales.
    """
    palabras = limpiar_y_tokenizar(texto)
    total_palabras = len(palabras)
    palabras_unicas = tuple(sorted(set(palabras)))
    ppm = calcular_ppm(total_palabras, duracion_segundos)

    return MetricasTurno(
        total_palabras=total_palabras,
        duracion_segundos=duracion_segundos,
        palabras_por_minuto=ppm,
        palabras_unicas=palabras_unicas
    )


def clasificar_nivel(ppm_promedio: float, total_palabras: int) -> str:
    """
    Determina el nivel alcanzado mediante Pattern Matching / Condiciones funcionales.
    """
    match (ppm_promedio, total_palabras):
        case (ppm, palabras) if ppm >= 90 and palabras >= 50:
            return "Advanced (Fluent & Dynamic)"
        case (ppm, palabras) if ppm >= 50 and palabras >= 25:
            return "Intermediate (Good Flow)"
        case _:
            return "Developing (Building Confidence)"


def generar_reporte_sesion(historial: Tuple[Turno, ...]) -> ReporteFinal:
    """
    Genera el reporte final de la sesión a través de pipelines funcionales (filter, map, reduce).
    """
    # 1. Filtrar solo los turnos del usuario (HOF: filter)
    turnos_usuario = tuple(filter(lambda t: t.emisor == "user", historial))
    
    if not turnos_usuario:
        return ReporteFinal(
            total_turnos_usuario=0,
            total_palabras=0,
            ppm_promedio=0.0,
            vocabulario_utilizado=(),
            feedback_gramatical=("No speech turns detected in this session.",),
            sugerencias_mejora=("Try responding in English to complete the roleplay.",),
            calificacion_general="Not Available"
        )

    # 2. Extraer métricas de cada turno (HOF: map)
    metricas_turnos = tuple(map(lambda t: analizar_turno_usuario(t.texto, t.duracion_segundos), turnos_usuario))

    # 3. Reducción para calcular totales (HOF: reduce)
    total_palabras = reduce(lambda acc, m: acc + m.total_palabras, metricas_turnos, 0)
    total_duracion = reduce(lambda acc, m: acc + m.duracion_segundos, metricas_turnos, 0.0)

    # 4. Vocabulario único consolidado (Comprensión funcional)
    vocabulario = tuple(sorted({palabra for m in metricas_turnos for palabra in m.palabras_unicas}))

    # 5. Promedio ponderado de PPM
    ppm_promedio = calcular_ppm(total_palabras, total_duracion)

    # 6. Clasificación
    nivel = clasificar_nivel(ppm_promedio, total_palabras)

    # 7. Sugerencias basadas en el análisis funcional
    sugerencias = []
    if ppm_promedio < 40:
        sugerencias.append("Try speaking in complete sentences rather than short phrases to boost your PPM.")
    if len(vocabulario) < 15:
        sugerencias.append("Expand your vocabulary by using more descriptive adjectives.")
    if not sugerencias:
        sugerencias.append("Great conversation flow! Keep maintaining this conversational pace.")

    return ReporteFinal(
        total_turnos_usuario=len(turnos_usuario),
        total_palabras=total_palabras,
        ppm_promedio=ppm_promedio,
        vocabulario_utilizado=vocabulario,
        feedback_gramatical=(
            "Session completed without critical conversational breakdowns.",
            f"Detected active vocabulary size of {len(vocabulario)} unique terms."
        ),
        sugerencias_mejora=tuple(sugerencias),
        calificacion_general=nivel
    )
